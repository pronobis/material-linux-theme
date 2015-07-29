material-linux-theme
====================

Auto-generated set of consistent themes for a Linux desktop based on the Android Material
color palette. The goal is to easily generate matching themes for all the apps in your
Linux desktop. Currently only a dark theme is provided.

The theme generator depends on the [python-256](https://github.com/magarcia/python-x256)
package.

Themes for the following apps are available at this point:
* GTK 2.0
* GTK 3.0
* i3 window manager
* Emacs
* Midnight Commander


Design
------

```
                                  +--------------------------------+
                                  |     for specific use-cases     |
                                  |                               \|/
raw_colors --> color_names --> palette --> common_theme --> [app_theme]+

<          Fixed         >     <   Defines the Theme  >     <  Fixed  >
```

* `raw_colors` - Raw color values
* `color_names` - Human-friendly color names of the Material color palette
* `palette` - Selects a subset of colors used in the theme
* `common_theme` - Assigns palette colors to common use-cases, provides unified look
  across all the applications
* `app_theme` - Multiple application specific themes that assigns colors to application-specific UI elements


### Palette ###

The palette consists of the following entries:
- `bg` - background color
- `fg` - foreground color (mostly text)
- `primary` - primary UI element color
- `secondary` - secondary UI element color
- `accent1` - first accent color
- `accent2` - second accent color
- `success`, `warning`, `error` - colors associated with states
- `semantic1` - `semantic11` - colors used to indicate various semantics, e.g. for syntax highlighting or file type indication in file managers
- ANSI colors, e.g. `red`, `light-red`, `dark-red` - colors assigned to ANSI color names for all use-cases requiring a specific color (e.g. in a terminal)

Most colors in the palette can have 3 variants:
- `normal` - nominal color
- `weak` - providing lower contrast on the background (e.g. darker variant in dark theme and lighter variant in light theme)
- `strong` - providing higher contrast on the background (e.g. lighter variant in dark theme and darker variant in light theme)
