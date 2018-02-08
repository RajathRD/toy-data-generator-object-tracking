import matplotlib.pyplot as plt
import matplotlib.patches as patches

# path to sequence file
seq_file_path = "./data/seq-1.csv"
seq_file_data = open(seq_file_path).read().split()

# data is converted back to it's original properties
data = [map(int, i.split(",")) for i in seq_file_data]

# extrack frame numbers
frame_nos = set([i[0] for i in data])

print frame_nos

# each frame is drawn
for frame in frame_nos:
    # extract each bbox
    bboxes = [row[-4:] for row in data if row[0] == frame]
    
    # empty canvas
    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.set_xlim([0, 256])
    ax.set_ylim([0, 256])
    ax.axis("off")

    # draw rectangles
    for rect in bboxes:
        print rect
        ax.add_patch(
            patches.Rectangle(
                # few adjustments to y-axis as plots have point(0, 0) at bottom-left corner, but in images, point(0, 0) is at top-left
                (rect[0], 256-rect[1]),
                (rect[2]-rect[0]),
                -(rect[3]-rect[1]),
                fill = False
                # TODO: need to randomly generate a edgecolor for each track_id and set it here, this should be done in the start
                # edgecolor="red"
            )
        )
    plt.show()


# to save figure as image
# frame_fname = "frame.png"
# fig.savefig(frame_fname, dpi=90, bbox_inches='tight')