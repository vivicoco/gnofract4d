# toolbar code

from gi.repository import Gtk

class T(Gtk.Toolbar):
    def __init__(self):
        Gtk.Toolbar.__init__(self)

        self.set_border_width(1)

    def add_space(self):
        self.insert(Gtk.SeparatorToolItem(), -1)

    def add_widget(self, widget, tip_text, private_text, expand=False):
        toolitem = Gtk.ToolItem()
        toolitem.add(widget)
        toolitem.set_expand(expand)
        toolitem.set_homogeneous(False)
        toolitem.set_tooltip_text(tip_text)
        self.insert(toolitem,-1)

    def add_button(self, title, tip_text, image, cb):
        try:
            toolitem = Gtk.ToolButton.new(image,title)
            self.insert(toolitem,-1)
        except:
            self.append_element(
                Gtk.ToolbarStyle.CHILD_BUTTON,
                None,
                title,
                tip_text,
                None,
                image,
                cb,
                None)

    def add_stock(self, stock_id, tip_text, cb):
        toolitem = Gtk.ToolButton.new_from_stock(stock_id)
        toolitem.connect('clicked', cb)
        toolitem.set_tooltip_text(tip_text)
        self.insert(toolitem,-1)

    def add_toggle(self, stock_id, title, tip_text, cb):
        toolitem = Gtk.ToggleToolButton.new_from_stock(stock_id)
        toolitem.connect('toggled', cb)
        toolitem.set_tooltip_text(tip_text)
        self.insert(toolitem,-1)
        return toolitem
