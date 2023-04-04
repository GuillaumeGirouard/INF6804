def IoU(box_gt, box_dt):
    # determine the (x, y)-coordinates of the intersection rectangle
	xA = max(box_gt[0], box_dt[0])
	yA = max(box_gt[1], box_dt[1])
	xB = min(box_gt[2], box_dt[2])
	yB = min(box_gt[3], box_dt[3])
	# compute the area of intersection rectangle
	interArea = max(0, xB - xA + 1) * max(0, yB - yA + 1)
	# compute the area of both the prediction and ground-truth
	# rectangles
	box_gtArea = (box_gt[2] - box_gt[0] + 1) * (box_gt[3] - box_gt[1] + 1)
	box_dtArea = (box_dt[2] - box_dt[0] + 1) * (box_dt[3] - box_dt[1] + 1)
	# compute the intersection over union by taking the intersection
	# area and dividing it by the sum of prediction + ground-truth
	# areas - the interesection area
	iou = interArea / float(box_gtArea + box_dtArea - interArea)
	# return the intersection over union value
	return iou

#exemple
#presente sous format xmin,ymin,xmax,ymax
#box_gt = (344,200,670,450)
#box_dt = (350,200,650,420)
#print(IoU(box_gt,box_dt))