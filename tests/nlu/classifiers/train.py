# -*- coding: utf-8 -*-
'''
@time: 2020/11/30 下午8:30
@author: xiaolin_peter
@contact: xiaolin_peter@163.com
@File train.py
'''

from rasa.nlu import train
from rasa.nlu.config import RasaNLUModelConfig
from rasa.nlu.components import ComponentBuilder
from rasa.nlu.model import Interpreter
import asyncio

EPOCHS = "epochs"
RANDOM_SEED = "random_seed"
BILOU_FLAG = "BILOU_flag"


def as_pipeline(*components):
    return [{"name": c} for c in components]


async def train_persist_load_with_composite_entities(classifier_params, component_builder, model_path):
    # pipeline = as_pipeline(
    #     "WhitespaceTokenizer", "CountVectorsFeaturizer", "DIETClassifier"
    # )

    pipeline = as_pipeline("MitieNLP", "JiebaTokenizer", "MitieEntityExtractor",
                           "MitieFeaturizer", "SklearnIntentClassifier")
    assert pipeline[4]["name"] == "SklearnIntentClassifier"
    pipeline[4].update(classifier_params)

    _config = RasaNLUModelConfig({"pipeline": pipeline, "language": "cn"})

    (trainer, trained, persisted_path) = await train(
        _config,
        path=model_path,
        data="../../../data/test/demo-rasa-zh.json",
        component_builder=component_builder,
    )

    assert trainer.pipeline
    assert trained.pipeline

    loaded = Interpreter.load(persisted_path, component_builder)

    assert loaded.pipeline
    text = "感冒发烧了怎么办"
    print("--------------------------------------------------")
    print(trained.parse(text))
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("++++++++++++++++++++++++++++++++++++++++++++++++++")
    print(loaded.parse(text))
    print("--------------------------------------------------")
    assert loaded.parse(text) == trained.parse(text)


if __name__ == '__main__':
    # test_train_model_checkpointing_peter()
    classifier_params = {RANDOM_SEED: 1, EPOCHS: 1, BILOU_FLAG: False}
    loop = asyncio.get_event_loop()
    res = loop.run_until_complete(train_persist_load_with_composite_entities(classifier_params,                                                                      ComponentBuilder(), "../models"))
    loop.close()
