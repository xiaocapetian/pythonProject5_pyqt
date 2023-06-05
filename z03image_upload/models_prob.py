from tensorflow.keras import layers, Sequential, applications
from tensorflow.keras.models import Model


def branch_net(func):
    input1 = layers.Input(shape=(80, 80, 3))
    input2 = layers.Input(shape=(80, 80, 1))

    model1 = func(include_top=False, weights='imagenet', input_shape=(80, 80, 3), pooling='max')
    # include_top=False不要模型最后的密集链接分类器
    flu_branch = model1(input1)
    flu_branch = layers.Dense(256, activation='relu')(flu_branch)
    flu_branch = layers.Dropout(0.5)(flu_branch)
    flu_branch = layers.Dense(128, activation='relu')(flu_branch)

    model2 = func(include_top=False, weights=None, input_shape=(80, 80, 1), pooling='max')
    model2._name = model2.name + '_1'
    w_branch = model2(input2)
    w_branch = layers.Dense(256, activation='relu')(w_branch)
    w_branch = layers.Dropout(0.5)(w_branch)
    w_branch = layers.Dense(128, activation='relu')(w_branch)

    combined = layers.concatenate([flu_branch, w_branch])
    output = layers.Dense(256, activation='relu')(combined)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(128, activation='relu')(output)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(1, activation='sigmoid')(output)
    model = Model(inputs=[input1, input2], outputs=output)
    # model.summary()
    return model


def se_block(channels, ratio, inputs):
    output = layers.Conv2D(channels, 3, (1, 1), padding='same')(inputs)
    output = layers.BatchNormalization()(output)
    output = layers.ReLU()(output)
    output = layers.MaxPool2D()(output)
    se = layers.GlobalAveragePooling2D()(output)
    se = layers.Dense(channels // ratio, activation='relu', kernel_initializer='he_normal', use_bias=False)(se)
    se = layers.Dense(channels, activation='sigmoid', kernel_initializer='he_normal', use_bias=False)(se)
    output = layers.multiply([output, se])
    return output


def ctc_se(ratio=2, droprate=0.5, feature1=128, feature2=64):
    input1 = layers.Input(shape=(80, 80, 3))
    input2 = layers.Input(shape=(80, 80, 1))

    flu = se_block(16, ratio, input1)
    flu = se_block(32, ratio, flu)
    fl = se_block(64, ratio, flu)
    flu = se_block(128, ratio, flu)
    flu = layers.Flatten()(flu)
    flu = layers.Dense(256, activation='relu')(flu)
    flu = layers.Dropout(droprate)(flu)
    flu = layers.Dense(feature1, activation='relu')(flu)

    w = se_block(16, ratio, input2)
    w = se_block(32, ratio, w)
    w = se_block(64, ratio, w)
    w = se_block(128, ratio, w)
    w = layers.Flatten()(w)
    w = layers.Dense(256, activation='relu')(w)
    w = layers.Dropout(droprate)(w)
    w = layers.Dense(feature2, activation='relu')(w)

    combined = layers.concatenate([flu, w])
    output = layers.Dense(256, activation='relu')(combined)
    output = layers.Dropout(droprate)(output)
    output = layers.Dense(128, activation='relu')(output)
    output = layers.Dropout(droprate)(output)
    output = layers.Dense(1, activation='sigmoid')(output)
    model = Model(inputs=[input1, input2], outputs=output)
    # model.summary()
    return model


def ctc():
    flu_branch = Sequential(
        [layers.Input(shape=(80, 80, 3)),
         layers.Conv2D(16, 3, (1, 1), padding='same', activation='relu'),
         # layers.Conv2D（卷积核个数，卷积核的大小，strides=(1, 1)步长，padding填充）
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Conv2D(32, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Conv2D(64, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Conv2D(128, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Flatten(),
         layers.Dense(256, activation='relu'),
         layers.Dropout(0.5),
         layers.Dense(128, activation='relu'), ]
    )
    w_branch = Sequential(
        [layers.Input(shape=(80, 80, 1)),
         layers.Conv2D(16, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Conv2D(32, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Conv2D(64, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Conv2D(128, 3, (1, 1), padding='same', activation='relu'),
         layers.BatchNormalization(),
         layers.MaxPool2D(),
         layers.Flatten(),
         layers.Dense(256, activation='relu'),
         layers.Dropout(0.5),
         layers.Dense(64, activation='relu'), ]
    )
    combined = layers.concatenate([flu_branch.output, w_branch.output])
    output = layers.Dense(256, activation='relu')(combined)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(128, activation='relu')(output)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(1, activation='sigmoid')(output)
    model = Model(inputs=[flu_branch.input, w_branch.input], outputs=output)
    # model.summary()
    return model


def feature(inputs):
    output = se_block(16, 4, inputs)
    output = se_block(32, 4, output)
    output = se_block(64, 4, output)
    output = se_block(128, 4, output)
    output = layers.Flatten()(output)
    return output


def stack_net(func):
    inputs = layers.Input(shape=(80, 80, 4))
    if func is None:
        output = feature(inputs)
    else:
        model = func(include_top=False, weights=None, input_shape=(80, 80, 4), pooling='max')
        output = model(inputs)
    output = layers.Dense(256, activation='relu')(output)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(128, activation='relu')(output)
    output = layers.Dense(256, activation='relu')(output)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(128, activation='relu')(output)
    output = layers.Dropout(0.5)(output)
    output = layers.Dense(1, activation='sigmoid')(output)
    model = Model(inputs=inputs, outputs=output)
    return model


if __name__ == '__main__':
    se_ctcnet = ctc_se()
    ctcnet = ctc()
    xception = branch_net(applications.Xception)
    resnet50v2 = branch_net(applications.ResNet50V2)
    inceptionv3 = branch_net(applications.InceptionV3)
    densenet121 = branch_net(applications.DenseNet121)
