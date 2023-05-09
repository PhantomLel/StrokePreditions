import random


def RF(train, test):
    import tensorflow_decision_forests as tfdf

    m = tfdf.keras.RandomForestModel(
        num_trees=60, verbose=0, random_seed=random.randint(0, 1000)
    )

    m.fit(train, verbose=0)
    m.compile(metrics=["accuracy"])
    # return test and self eval scores
    return (
        m.evaluate(test, return_dict=True, verbose=0)["accuracy"],
        m.make_inspector().evaluation(),
    )


def linear_regression(train, test):
    import tensorflow as tf

    model = tf.keras.models.Sequential(
        [
            tf.keras.layers.Dense(2, activation="relu", name="layer1"),
            tf.keras.layers.Dense(3, activation="relu", name="layer2"),
            tf.keras.layers.Dense(4, name="layer3"),
        ]
    )
    
