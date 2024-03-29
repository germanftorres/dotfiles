# My awesome qtile configuration

from typing import List  # noqa: F401

from libqtile import qtile
from libqtile import bar, layout
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal

from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration, PowerLineDecoration

mod = "mod4"
terminal = guess_terminal()
browser = "brave-beta"

keys = [

    # essential tools
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch terminal"),

    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html

    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),

    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(),
        desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(),
        desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(),
        desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),

    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(),
        desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(),
        desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),

    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(), desc="Toggle between split and unsplit sides of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "w", lazy.window.kill(), desc="Kill focused window"),

    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(),
        desc="Spawn a command using a prompt widget"),
]

# groups = [Group(i) for i in "123456789"]

groups = [Group("1 term", layout="columns"),
    Group("2 editor", layout="columns"),
    Group("3 www", layout="columns"),
    Group("a", layout="columns"),
    Group("b", layout="columns"),


]

from libqtile.dgroups import simple_key_binder
dgroups_key_binder = simple_key_binder(mod)

# for i in groups:
#     keys.extend([
#         # mod1 + letter of group = switch to group
#         Key([mod], i.name, lazy.group[i.name].toscreen(),
#             desc="Switch to group {}".format(i.name)),

#         # mod1 + shift + letter of group = switch to & move focused window to group
#         Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
#             desc="Switch to & move focused window to group {}".format(i.name)),
#         # Or, use below if you prefer not to switch to that group.
#         # # mod1 + shift + letter of group = move focused window to group
#         # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
#         #     desc="move focused window to group {}".format(i.name)),
#     ])


layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }


layouts = [
    layout.Columns(**layout_theme),
    # layout.Columns(border_focus_stack=['#d75f5f', '#8f3d3d'], border_width=4),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]


colors = [["#282c34", "#282c34"],
          ["#1c1f24", "#1c1f24"],
          ["#dfdfdf", "#dfdfdf"],
          ["#ff6c6b", "#ff6c6b"],
          ["#98be65", "#98be65"],
          ["#da8548", "#da8548"],
          ["#51afef", "#51afef"],
          ["#c678dd", "#c678dd"],
          ["#46d9ff", "#46d9ff"],
          ["#a9a1e1", "#a9a1e1"]]


widget_defaults = dict(
    font="Noto Sans Bold",
    fontsize=18,
    padding=2,
    background=colors[1]
)

decorations = {
    "decorations": [
        PowerLineDecoration(path="arrow_right")
    ]
}

extension_defaults = widget_defaults.copy()

def init_widgets_list():
    widget_list = [
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[2],
            background = colors[0]
            ),
        widget.GroupBox(
            font = "Noto Sans Bold",
            fontsize = 16,
            margin_y = 3,
            margin_x = 0,
            padding_y = 5,
            padding_x = 3,
            borderwidth = 3,
            active = colors[2],
            inactive = colors[4],
            rounded = False,
            highlight_color = colors[1],
            highlight_method = "line",
            this_current_screen_border = colors[6],
            this_screen_border = colors [4],
            other_current_screen_border = colors[6],
            other_screen_border = colors[4],
            foreground = colors[2],
            background = colors[0]
            ),
        widget.TextBox(
                text = '|',
                font = "Noto Sans Bold",
                background = colors[0],
                foreground = '474747',
                padding = 2,
                fontsize = 16
                ),            
        widget.WindowName(
                foreground = colors[6],
                background = colors[0],
                padding = 0
                ),            
        # widget.Spacer(),                
        widget.CurrentLayout(
            foreground = colors[2],
            background = colors[0],
            padding = 5            
            ),
        # widget.Systray(
        #     background = colors[0],
        #     padding = 5
        #     ),
        # widget.ThermalSensor(
        #     foreground = colors[4],
        #     background = colors[0],
        #     threshold = 90,
        #     fmt = 'Temp: {}',
        #     padding = 5,
        #     decorations=[
        #         BorderDecoration(
        #             colour = colors[4],
        #             border_width = [0, 0, 2, 0],
        #             padding_x = 5,
        #             padding_y = None,
        #         )
        #     ],
        #     ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0],
            **decorations            
            ),            
        widget.Memory(
            foreground = colors[9],
            background = colors[1],
            mouse_callbacks = {'Button1': lambda: qtile.cmd_spawn(terminal + ' -e htop')},
            fmt = 'Mem: {}',
            padding = 5,
            **decorations,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0],
            **decorations,
            ),                    
        widget.Volume(
            foreground = colors[7],
            background = colors[1],
            fmt = 'Vol: {}',
            padding = 5,
            **decorations,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0],
            **decorations,
            ),
        widget.KeyboardLayout(
            configured_keyboards = ['es', 'us'],
            foreground = colors[8],
            background = colors[0],
            fmt = 'Keyboard: {}',
            padding = 5,
            **decorations,
            ),
        widget.Sep(
            linewidth = 0,
            padding = 6,
            foreground = colors[0],
            background = colors[0],
            **decorations,            
            ),
        # widget.AnalogueClock(
        #         background = colors[0],
        #         face_shape = "square",
        #         face_background = colors[6],
        #         face_border_colour = colors[6],
        #         face_border_width = 4,
        #         padding = 5
        #         ),
        widget.Clock(
                foreground = colors[6],
                background = colors[0],
                format = "%c",
                          
                ),
        # widget.Sep(
        #         linewidth = 0,
        #         padding = 6,
        #         foreground = colors[0],
        #         background = colors[0]
        #         ),        

    ]
    return widget_list


# pepe_list = init_widgets_list()

screens = [

    Screen(top=bar.Bar(widgets=init_widgets_list(), size=24)),
    # Screen(

    #     top=bar.Bar(
    #         [

    #             widget.GroupBox(),
    #             widget.Prompt(),
    #             widget.WindowName(),
    #             widget.Chord(
    #                 chords_colors={
    #                     'launch': ("#ff0000", "#ffffff"),
    #                 },
    #                 name_transform=lambda name: name.upper(),
    #             ),
    #             widget.TextBox("my config 2", name="default"),
    #             widget.TextBox("Press &lt;M-r&gt; to spawn", foreground="#d75f5f"),
    #             widget.Systray(),
    #             widget.Clock(format='%Y-%m-%d %a %I:%M %p'),
    #             widget.QuickExit(),
    #         ],
    #         24,
    #         # border_width=[2, 0, 2, 0],  # Draw top and bottom borders
    #         # border_color=["ff00ff", "000000", "ff00ff", "000000"]  # Borders are magenta
    #     ),
    #),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# dgroups_key_binder = None
dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    *layout.Floating.default_float_rules,
    Match(wm_class='confirmreset'),  # gitk
    Match(wm_class='makebranch'),  # gitk
    Match(wm_class='maketag'),  # gitk
    Match(wm_class='ssh-askpass'),  # ssh-askpass
    Match(title='branchdialog'),  # gitk
    Match(title='pinentry'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
