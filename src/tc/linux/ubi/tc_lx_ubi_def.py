# SPDX-License-Identifier: GPL-2.0
#
# Description:
# simply set defaults for linux ubi tests
#
# used variables
#
# - tb.config.tc_ubi_cmd_path
#| path to ubi commands (in mtd-utils package)
#| default: '/work/tbot/mtd-utils'
#
# - tb.config.tc_ubi_mtd_dev
#| mtd device used
#| default: '/dev/mtd4'
#
# - tb.config.tc_ubi_ubi_dev
#| ubi device used
#| default: '/dev/ubi0'
#
# - tb.config.tc_ubi_min_io_size
#| ubi minimum io size
#| http://www.linux-mtd.infradead.org/faq/ubi.html#L_find_min_io_size
#| default: '1024'
#
# - tb.config.tc_ubi_max_leb_cnt
#| used leb number
#| default: '100'
#
# - tb.config.tc_ubi_leb_size
#| http://www.linux-mtd.infradead.org/faq/ubi.html#L_find_min_io_size
#| default: '126976'
#
# - tb.config.tc_ubi_vid_hdr_offset
#| http://www.linux-mtd.infradead.org/doc/ubi.html#L_ubi_headers
#| http://www.linux-mtd.infradead.org/faq/ubi.html#L_vid_offset_mismatch
#| default: 'default'
#
# - tb.config.tc_lx_ubi_format_filename
#| filename for ubiformat
#| default: '/home/hs/ccu1/ecl-image-usbc.ubi'
#
# End:

from tbotlib import tbot

tb.define_variable('tc_ubi_cmd_path', '/work/tbot/mtd-utils')
tb.define_variable('tc_ubi_mtd_dev', '/dev/mtd4')
tb.define_variable('tc_ubi_ubi_dev', '/dev/ubi0')
tb.define_variable('tc_ubi_min_io_size', '1024')
tb.define_variable('tc_ubi_max_leb_cnt', '100')
tb.define_variable('tc_ubi_leb_size', '126976')
tb.define_variable('tc_ubi_vid_hdr_offset', 'default')
tb.define_variable('tc_lx_ubi_format_filename', '/home/hs/ccu1/ecl-image-usbc.ubi')

tb.end_tc(True)
