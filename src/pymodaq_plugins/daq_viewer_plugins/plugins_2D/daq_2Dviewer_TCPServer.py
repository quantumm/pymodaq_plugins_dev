from qtpy.QtCore import Signal, Slot
from easydict import EasyDict as edict
from collections import OrderedDict
from pymodaq.daq_viewer.utility_classes import DAQ_Viewer_TCP_server
from pymodaq.daq_utils.daq_utils import ThreadCommand, getLineInfo, DataFromPlugins, Axis


class DAQ_2DViewer_TCPServer(DAQ_Viewer_TCP_server):
    """
        ================= ==============================
        **Attributes**      **Type**
        *command_server*    instance of Signal
        *x_axis*            1D numpy array
        *y_axis*            1D numpy array
        *data*              double precision float array
        ================= ==============================

        See Also
        --------
        utility_classes.DAQ_TCP_server
    """
    params_GRABBER = []

    # params = DAQ_TCP_server.params

    command_server = Signal(list)

    # params=DAQ_TCP_server.params
    def __init__(self, parent=None, params_state=None):
        super().__init__(parent, params_state,
                         grabber_type='2D')  # initialize base class with commom attributes and methods

        self.x_axis = None
        self.y_axis = None
        self.data = None

    @Slot(list)
    def data_ready(self, data):
        """
            Send the grabed data signal.
        """
        self.data_grabed_signal.emit([DataFromPlugins(name='TCP Server 2D', data=data, type='Data2D')])
