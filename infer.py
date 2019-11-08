import cv2
import torch
from skimage import io
from skimage import transform


precision = 'fp32'

def init_model():
    ssd_model = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd', model_math=precision)
    utils = torch.hub.load('NVIDIA/DeepLearningExamples:torchhub', 'nvidia_ssd_processing_utils')

    ssd_model.to('cuda')
    ssd_model.eval()

    classes_to_labels = utils.get_coco_object_dictionary()

    return ssd_model, utils, classes_to_labels

def locate_object(frame, obj_of_interest, ssd_model, utils, classes_to_labels):
    cv2.imwrite("current.jpg", frame)
    uris = ["current.jpg"]

    inputs = [utils.prepare_input(uri) for uri in uris]
    tensor = utils.prepare_tensor(inputs, precision == 'fp16')

    with torch.no_grad():
        detections_batch = ssd_model(tensor)

    results_per_input = utils.decode_results(detections_batch)
    best_results_per_input = [utils.pick_best(results, 0.40) for results in results_per_input]

    for image_idx in range(len(best_results_per_input)):
        bboxes, classes, confidences = best_results_per_input[image_idx]
        for idx in range(len(bboxes)):
            if classes_to_labels[classes[idx] - 1] == obj_of_interest:
                left, bot, right, top = bboxes[idx]
                x, y, w, h = [val * 300 for val in [left, bot, right - left, top - bot]]
                #print("x:{} y:{} w:{} h:{} label:{} conf:{}".format(x, y, w, h, classes_to_labels[classes[idx] - 1], confidences[idx]*100))
                return x, y, w, h

    return None, None, None, None
