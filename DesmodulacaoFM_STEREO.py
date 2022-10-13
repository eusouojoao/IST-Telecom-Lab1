#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#
# SPDX-License-Identifier: GPL-3.0
#
# GNU Radio Python Flow Graph
# Title: Desmodulação FM STEREO
# GNU Radio version: v3.11.0.0git-244-g7c7894df

from packaging.version import Version as StrictVersion

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print("Warning: failed to XInitThreads()")

from PyQt5 import Qt
from gnuradio import qtgui
from gnuradio.filter import firdes
import sip
from gnuradio import analog
from gnuradio import audio
from gnuradio import blocks
import pmt
from gnuradio import filter
from gnuradio import gr
from gnuradio.fft import window
import sys
import signal
from argparse import ArgumentParser
from gnuradio.eng_arg import eng_float, intx
from gnuradio import eng_notation



from gnuradio import qtgui

class DesmodulacaoFM_STEREO(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Desmodulação FM STEREO ", catch_exceptions=True)
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Desmodulação FM STEREO ")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "DesmodulacaoFM_STEREO")

        try:
            if StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
                self.restoreGeometry(self.settings.value("geometry").toByteArray())
            else:
                self.restoreGeometry(self.settings.value("geometry"))
        except:
            pass

        ##################################################
        # Variables
        ##################################################
        self.samp_rate = samp_rate = 125000
        self.ratio = ratio = 125
        self.FM_station = FM_station = 104300000

        ##################################################
        # Blocks
        ##################################################
        self.rational_resampler_xxx_1_0 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=ratio,
                taps=[],
                fractional_bw=0)
        self.rational_resampler_xxx_1 = filter.rational_resampler_fff(
                interpolation=48,
                decimation=ratio,
                taps=[],
                fractional_bw=0)
        self.qtgui_freq_sink_x_3 = qtgui.freq_sink_c(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "PLL regenerated carrier", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_3.set_update_time(0.10)
        self.qtgui_freq_sink_x_3.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_3.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_3.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_3.enable_autoscale(False)
        self.qtgui_freq_sink_x_3.enable_grid(False)
        self.qtgui_freq_sink_x_3.set_fft_average(1.0)
        self.qtgui_freq_sink_x_3.enable_axis_labels(True)
        self.qtgui_freq_sink_x_3.enable_control_panel(False)
        self.qtgui_freq_sink_x_3.set_fft_window_normalized(False)



        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_3.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_3.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_3.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_3.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_3.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_3_win = sip.wrapinstance(self.qtgui_freq_sink_x_3.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_3_win)
        self.qtgui_freq_sink_x_1 = qtgui.freq_sink_f(
            1024, #size
            window.WIN_BLACKMAN_hARRIS, #wintype
            0, #fc
            samp_rate, #bw
            "DSB-SC L-R (freq. domain)", #name
            1,
            None # parent
        )
        self.qtgui_freq_sink_x_1.set_update_time(0.10)
        self.qtgui_freq_sink_x_1.set_y_axis((-140), 10)
        self.qtgui_freq_sink_x_1.set_y_label('Relative Gain', 'dB')
        self.qtgui_freq_sink_x_1.set_trigger_mode(qtgui.TRIG_MODE_FREE, 0.0, 0, "")
        self.qtgui_freq_sink_x_1.enable_autoscale(False)
        self.qtgui_freq_sink_x_1.enable_grid(False)
        self.qtgui_freq_sink_x_1.set_fft_average(1.0)
        self.qtgui_freq_sink_x_1.enable_axis_labels(True)
        self.qtgui_freq_sink_x_1.enable_control_panel(False)
        self.qtgui_freq_sink_x_1.set_fft_window_normalized(False)


        self.qtgui_freq_sink_x_1.set_plot_pos_half(not True)

        labels = ['', '', '', '', '',
            '', '', '', '', '']
        widths = [1, 1, 1, 1, 1,
            1, 1, 1, 1, 1]
        colors = ["blue", "red", "green", "black", "cyan",
            "magenta", "yellow", "dark red", "dark green", "dark blue"]
        alphas = [1.0, 1.0, 1.0, 1.0, 1.0,
            1.0, 1.0, 1.0, 1.0, 1.0]

        for i in range(1):
            if len(labels[i]) == 0:
                self.qtgui_freq_sink_x_1.set_line_label(i, "Data {0}".format(i))
            else:
                self.qtgui_freq_sink_x_1.set_line_label(i, labels[i])
            self.qtgui_freq_sink_x_1.set_line_width(i, widths[i])
            self.qtgui_freq_sink_x_1.set_line_color(i, colors[i])
            self.qtgui_freq_sink_x_1.set_line_alpha(i, alphas[i])

        self._qtgui_freq_sink_x_1_win = sip.wrapinstance(self.qtgui_freq_sink_x_1.qwidget(), Qt.QWidget)
        self.top_layout.addWidget(self._qtgui_freq_sink_x_1_win)
        self.low_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.low_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.low_pass(
                1,
                samp_rate,
                15000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.blocks_sub_xx_0 = blocks.sub_ff(1)
        self.blocks_multiply_xx_1 = blocks.multiply_vff(1)
        self.blocks_multiply_xx_0 = blocks.multiply_vcc(1)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_float*1, '/home/joao/Documents/MEEC/3o ano/1 sem/Telecom/Lab/Lab1/Testes/LEFT_POSD_1000Hz.dat', True, 0, 0)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self.blocks_complex_to_real_1 = blocks.complex_to_real(1)
        self.blocks_add_xx_0 = blocks.add_vff(1)
        self.band_pass_filter_2 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                37000,
                39000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_1 = filter.fir_filter_fff(
            1,
            firdes.band_pass(
                1,
                samp_rate,
                23000,
                53000,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.band_pass_filter_0 = filter.fir_filter_fcc(
            1,
            firdes.complex_band_pass(
                1,
                samp_rate,
                18500,
                19500,
                1000,
                window.WIN_HAMMING,
                6.76))
        self.audio_sink_0 = audio.sink(48000, '', True)
        self.analog_pll_refout_cc_0 = analog.pll_refout_cc(0.00065, 0.238886, 0.238635)


        ##################################################
        # Connections
        ##################################################
        self.connect((self.analog_pll_refout_cc_0, 0), (self.blocks_multiply_xx_0, 0))
        self.connect((self.analog_pll_refout_cc_0, 0), (self.blocks_multiply_xx_0, 1))
        self.connect((self.analog_pll_refout_cc_0, 0), (self.qtgui_freq_sink_x_3, 0))
        self.connect((self.band_pass_filter_0, 0), (self.analog_pll_refout_cc_0, 0))
        self.connect((self.band_pass_filter_1, 0), (self.blocks_multiply_xx_1, 1))
        self.connect((self.band_pass_filter_1, 0), (self.qtgui_freq_sink_x_1, 0))
        self.connect((self.band_pass_filter_2, 0), (self.blocks_multiply_xx_1, 0))
        self.connect((self.blocks_add_xx_0, 0), (self.audio_sink_0, 0))
        self.connect((self.blocks_complex_to_real_1, 0), (self.band_pass_filter_2, 0))
        self.connect((self.blocks_file_source_0, 0), (self.band_pass_filter_0, 0))
        self.connect((self.blocks_file_source_0, 0), (self.band_pass_filter_1, 0))
        self.connect((self.blocks_file_source_0, 0), (self.low_pass_filter_1, 0))
        self.connect((self.blocks_multiply_xx_0, 0), (self.blocks_complex_to_real_1, 0))
        self.connect((self.blocks_multiply_xx_1, 0), (self.low_pass_filter_2, 0))
        self.connect((self.blocks_sub_xx_0, 0), (self.audio_sink_0, 1))
        self.connect((self.low_pass_filter_1, 0), (self.rational_resampler_xxx_1, 0))
        self.connect((self.low_pass_filter_2, 0), (self.rational_resampler_xxx_1_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_add_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1, 0), (self.blocks_sub_xx_0, 0))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_add_xx_0, 1))
        self.connect((self.rational_resampler_xxx_1_0, 0), (self.blocks_sub_xx_0, 1))


    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "DesmodulacaoFM_STEREO")
        self.settings.setValue("geometry", self.saveGeometry())
        self.stop()
        self.wait()

        event.accept()

    def get_samp_rate(self):
        return self.samp_rate

    def set_samp_rate(self, samp_rate):
        self.samp_rate = samp_rate
        self.band_pass_filter_0.set_taps(firdes.complex_band_pass(1, self.samp_rate, 18500, 19500, 1000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_1.set_taps(firdes.band_pass(1, self.samp_rate, 23000, 53000, 1000, window.WIN_HAMMING, 6.76))
        self.band_pass_filter_2.set_taps(firdes.band_pass(1, self.samp_rate, 37000, 39000, 1000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_1.set_taps(firdes.low_pass(1, self.samp_rate, 15000, 1000, window.WIN_HAMMING, 6.76))
        self.low_pass_filter_2.set_taps(firdes.low_pass(1, self.samp_rate, 15000, 1000, window.WIN_HAMMING, 6.76))
        self.qtgui_freq_sink_x_1.set_frequency_range(0, self.samp_rate)
        self.qtgui_freq_sink_x_3.set_frequency_range(0, self.samp_rate)

    def get_ratio(self):
        return self.ratio

    def set_ratio(self, ratio):
        self.ratio = ratio

    def get_FM_station(self):
        return self.FM_station

    def set_FM_station(self, FM_station):
        self.FM_station = FM_station




def main(top_block_cls=DesmodulacaoFM_STEREO, options=None):

    if StrictVersion("4.5.0") <= StrictVersion(Qt.qVersion()) < StrictVersion("5.0.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()

    tb.start()

    tb.show()

    def sig_handler(sig=None, frame=None):
        tb.stop()
        tb.wait()

        Qt.QApplication.quit()

    signal.signal(signal.SIGINT, sig_handler)
    signal.signal(signal.SIGTERM, sig_handler)

    timer = Qt.QTimer()
    timer.start(500)
    timer.timeout.connect(lambda: None)

    qapp.exec_()

if __name__ == '__main__':
    main()
