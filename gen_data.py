"""
frame, track_id, type (0 = small, 1 = medium, 2 = large), bbox
"""
import numpy as np


def create_bbox(frame_width, frame_height, dimensions):
    """
        Function to output a bbox x,y co-ordinate of top-left vertex and bottom-right vertex
        Call : create_bbox(frame_with, frame_height, [width of bbox, height of bbox])
    """
    # Find a random position to place the box
    x = np.random.randint(0, frame_width - dimensions[0] - 1)    
    y = np.random.randint(0, frame_height - dimensions[1] - 1)

    return [x, y, x + dimensions[0], y + dimensions[1]]



def create_sequence(num_frames, frame_width, frame_height):
    """
        Creates a single sequence with small, medium or large objects. Sequences are also built
        randomly, that is, number of objects in each sequence is generated randomly
    """
    # Generate dimensions of small, medium and large bboxes
    small = (np.random.randint(10, 30), np.random.randint(10, 30))
    medium = (np.random.randint(40, 60), np.random.randint(40, 60))
    large = (np.random.randint(70, 90), np.random.randint(70, 90))
    shapes = [small, medium, large]

    # Generate number of each objects and build a sequence
    num_small = np.random.randint(1, 4)
    num_medium = np.random.randint(1, 2)
    num_large = np.random.randint(1, 2)

    # building a sequence, the index represents track_id and element represents object for that track_id
    track_id = [0 for i in range(num_small)] + [1 for i in range(num_medium)] + [2 for i in range(num_large)]
    
    sequence = [[i, j, track_id[j]] +  create_bbox(frame_width, frame_height, shapes[track_id[j]])
                 for i in range(num_frames)\
                 for j in range(len(track_id))]
               
    return sequence


def create_data(num_sequences, num_frames, frame_width, frame_height):
    """
        Creates multiple sequences at the same time
    """

    data = [create_sequence(num_frames, frame_width, frame_height) for i in range(num_sequences)]
    return data
    
def main():
    # Set parameters before running
    frame_width = 256
    frame_height = 256
    num_sequences = 2
    num_frames = 3

    # Directory where data need to be stored. Must be created before execution
    data_dir = "./data/"
    data = create_data(num_sequences, num_frames, frame_width, frame_height)
    
    # Data is dumped in .csv format
    for i in range(len(data)):
        seq_path = data_dir + "seq-" + str(i) + ".csv"
        seq_file = open(seq_path, "w")
        for j in data[i]:
            seq_file.write(",".join(map(str, j)) + "\n")
        seq_file.close()
    
if __name__=="__main__":
    main()