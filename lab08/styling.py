import PySide6.QtGui as QtG


LIGHT_PALETTE = QtG.QPalette()
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.WindowText, QtG.QColor(0, 0, 0, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Button, QtG.QColor(240, 240, 240, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Light, QtG.QColor(255, 255, 255, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Midlight, QtG.QColor(227, 227, 227, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Dark, QtG.QColor(160, 160, 160, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Mid, QtG.QColor(160, 160, 160, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Text, QtG.QColor(0, 0, 0, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.BrightText, QtG.QColor(255, 255, 255, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.ButtonText, QtG.QColor(0, 0, 0, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Base, QtG.QColor(255, 255, 255, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Window, QtG.QColor(240, 240, 240, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Shadow, QtG.QColor(105, 105, 105, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.HighlightedText, QtG.QColor(255, 255, 255, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.Link, QtG.QColor(0, 0, 255, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(255, 0, 255, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(245, 245, 245, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.NoRole, QtG.QColor(0, 0, 0, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.PlaceholderText, QtG.QColor(0, 0, 0, 128))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(255, 255, 220, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
LIGHT_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(0, 0, 0, 255))



DARK_PALETTE = QtG.QPalette()
DARK_PALETTE.setColor(QtG.QPalette.ColorRole.WindowText, QtG.QColor(255, 255, 255, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.WindowText, QtG.QColor(157, 157, 157, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Button, QtG.QColor(60, 60, 60, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Light, QtG.QColor(120, 120, 120, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Midlight, QtG.QColor(90, 90, 90, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Dark, QtG.QColor(30, 30, 30, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Mid, QtG.QColor(40, 40, 40, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Text, QtG.QColor(255, 255, 255, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Text, QtG.QColor(157, 157, 157, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.BrightText, QtG.QColor(255, 232, 69, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.ButtonText, QtG.QColor(255, 255, 255, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(157, 157, 157, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Base, QtG.QColor(45, 45, 45, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Base, QtG.QColor(30, 30, 30, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Window, QtG.QColor(30, 30, 30, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Shadow, QtG.QColor(0, 0, 0, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.Highlight, QtG.QColor(30, 30, 30, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.HighlightedText, QtG.QColor(255, 255, 255, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.Link, QtG.QColor(255, 185, 0, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Link, QtG.QColor(48, 140, 198, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(92, 33, 0, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(255, 0, 255, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(92, 33, 0, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(52, 52, 52, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.NoRole, QtG.QColor(0, 0, 0, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(255, 255, 220, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(0, 0, 0, 255))

DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.PlaceholderText, QtG.QColor(255, 255, 255, 128))






















# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.WindowText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.WindowText, QtG.QColor(157, 157, 157, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.WindowText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.WindowText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.WindowText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.WindowText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Button, QtG.QColor(60, 60, 60, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Light, QtG.QColor(120, 120, 120, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Midlight, QtG.QColor(90, 90, 90, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Dark, QtG.QColor(30, 30, 30, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Mid, QtG.QColor(40, 40, 40, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.Text, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Text, QtG.QColor(157, 157, 157, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.Text, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.Text, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.Text, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Text, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.BrightText, QtG.QColor(255, 232, 69, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(157, 157, 157, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.ButtonText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.Base, QtG.QColor(45, 45, 45, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Base, QtG.QColor(30, 30, 30, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.Base, QtG.QColor(45, 45, 45, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.Base, QtG.QColor(45, 45, 45, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.Base, QtG.QColor(45, 45, 45, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Base, QtG.QColor(45, 45, 45, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Window, QtG.QColor(30, 30, 30, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Shadow, QtG.QColor(0, 0, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.Highlight, QtG.QColor(30, 30, 30, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Highlight, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.HighlightedText, QtG.QColor(255, 255, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.Link, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.Link, QtG.QColor(48, 140, 198, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.Link, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.Link, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.Link, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.Link, QtG.QColor(255, 185, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(255, 0, 255, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.LinkVisited, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(52, 52, 52, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.AlternateBase, QtG.QColor(92, 33, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.NoRole, QtG.QColor(0, 0, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(255, 255, 220, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.ToolTipBase, QtG.QColor(60, 60, 60, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Active, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Disabled, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(0, 0, 0, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Inactive, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.NColorGroups, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.Current, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.ToolTipText, QtG.QColor(212, 212, 212, 255))
# DARK_PALETTE.setColor(QtG.QPalette.ColorGroup.All, QtG.QPalette.ColorRole.PlaceholderText, QtG.QColor(255, 255, 255, 128))
