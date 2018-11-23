# -*- coding: utf-8 -*-

"""Inception v3 architecture 모델을 retraining한 모델을 이용해서 이미지에 대한 추론(inference)을 진행하는 예제"""

import numpy as np
import tensorflow as tf

modelFullPath_season = '/tmp/output_graph_season.pb'                                      # 읽어들일 graph 파일 경로
labelsFullPath_season = '/tmp/output_labels_season.txt'                                   # 읽어들일 labels 파일 경로
modelFullPath_look = '/tmp/output_graph_look.pb'
labelsFullPath_look = '/tmp/output_labels_look.txt'

def create_graph_season():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    with tf.gfile.FastGFile(modelFullPath_season, 'rb') as f_season:
        graph_def_season = tf.GraphDef()
        graph_def_season.ParseFromString(f_season.read())
        __season = tf.import_graph_def(graph_def_season, name='')



def run_inference_on_image_season(imagePath):
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph_season()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-1:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(labelsFullPath_season, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]

        hash_list = []
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            hash_list.append(human_string)
            # print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]

        return hash_list



#######################################################################################
#look
def create_graph_look():
    """저장된(saved) GraphDef 파일로부터 graph를 생성하고 saver를 반환한다."""
    # 저장된(saved) graph_def.pb로부터 graph를 생성한다.
    tf.reset_default_graph()
    with tf.gfile.FastGFile(modelFullPath_look, 'rb') as f_look:
        graph_def_look = tf.GraphDef()
        graph_def_look.ParseFromString(f_look.read())
        __look = tf.import_graph_def(graph_def_look, name='')


def run_inference_on_image_look(imagePath):
    answer = None

    if not tf.gfile.Exists(imagePath):
        tf.logging.fatal('File does not exist %s', imagePath)
        return answer

    image_data = tf.gfile.FastGFile(imagePath, 'rb').read()

    # 저장된(saved) GraphDef 파일로부터 graph를 생성한다.
    create_graph_look()

    with tf.Session() as sess:

        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
        predictions = sess.run(softmax_tensor,
                               {'DecodeJpeg/contents:0': image_data})
        predictions = np.squeeze(predictions)

        top_k = predictions.argsort()[-1:][::-1]  # 가장 높은 확률을 가진 5개(top 5)의 예측값(predictions)을 얻는다.
        f = open(labelsFullPath_look, 'rb')
        lines = f.readlines()
        labels = [str(w).replace("\n", "") for w in lines]

        hash_list = []
        for node_id in top_k:
            human_string = labels[node_id]
            score = predictions[node_id]
            hash_list.append(human_string)
            # print('%s (score = %.5f)' % (human_string, score))

        answer = labels[top_k[0]]
        return hash_list

#look
