import argparse

def init_arguments():
    parser = argparse.ArgumentParser(prog='DL hw3: LeNet')

    # General
    parser.add_argument('--NonCNN', action='store_true')
    parser.add_argument('--random_state', type=int, default=4028)
    parser.add_argument('--verbose', action='store_true')
    parser.add_argument('--dataPATH', type=str, default='./data/', help='The path where should the data be loaded in.')
    parser.add_argument('--savePATH', type=str, default='./output/', help='The path to store the outputs, including models, plots, and training and evalution results.')
    parser.add_argument('--save_model', action='store_true', help='Whether to save the trained models')
    parser.add_argument('--save_trainer', action='store_true', default=True, help='Whether to save the trainer.')
    parser.add_argument('--model_name', type=str, default='lenet5', choices=['lenet5', 'improved_lenet5', 'CNN'], help='Which kind of model is going to be trained?')
    parser.add_argument('--resize', nargs='+', type=int, default=(64, 64), help='The target size of images')

    # Model structure
    parser.add_argument('--input_dim', nargs='+', type=int, default=[3, 64, 64], help='Dimension of the input image array')
    parser.add_argument('--num_conv_layers', type=int, default=2, help='No. of convolution layers')
    parser.add_argument('--nums_filter', nargs='+', type=int, default=[16, 16], help='List of no. of filters of each conv. layer. Its length should be same as num_conv_layers.')
    parser.add_argument('--sizes_filter', nargs='+', type=int, default=[5, 5], help='List of filter size of each conv. layer. Its length should be same as num_conv_layers.')
    parser.add_argument('--pads', nargs='+', type=int, default=[1, 1], help='List of padding elements for each conv. layer. Its length should be same as num_conv_layers.')
    parser.add_argument('--strides', nargs='+', type=int, default=[1, 1], help='List of no. of strides for each conv. layer. Its length should be same as num_conv_layers.')
    parser.add_argument('--pooling_size', type=int, default=2, help='Size of max pooling layer')
    parser.add_argument('--pooling_stride', type=int, default=1, help='No. of stride of max pooling layer')
    parser.add_argument('--hidden_sizes', nargs='+', type=int, default=[32, 16], help='Dimension of the hidden state of the linear layers')
    parser.add_argument('--hidden_act', type=str, default='Sigmoid', choices=['Sigmoid', 'ReLU', 'tanh'], help='Activation function of all hidden layers (except for the last layer)')
    
    # Training
    parser.add_argument('--optimizer', type=str, default='Adam', choices=['SGD', 'Momentum', 'AdaGrad', 'Adam'], help='Optimizer')
    parser.add_argument('--lr', type=float, default=0.01, help='Learning rate')
    parser.add_argument('--batch_size', type=int, default=64, help='Batch size')
    parser.add_argument('--epochs', type=int, default=30, help='No. of epochs')
    parser.add_argument('--print_result_per_epochs', type=int, default=5, help='How many epochs that the evaluated results be printed once?')
    parser.add_argument('--pretrained_model', type=str, default='', help='File name of the pretained model that is going to keep being trained or to be evaluated. Set an empty string if not using a pretrained model.')
    parser.add_argument('--plot_figsize', nargs='+', type=int, default=[8, 6], help='Figure size of model performance plot. Its length should be 2.')
    
    return parser