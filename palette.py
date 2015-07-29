# material-linux - Auto-generated set of consistent themes for a Linux
#                  desktop based on the Android Material color palette.
#
# Copyright (C) 2014 Andrzej Pronobis
# Author: Andrzej Pronobis <a.pronobis@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

palette = {
    # Background
    "bg-strong":          "#212121",
    "bg-normal":          "#121212",
    "bg-weak":            "#000000",
    # Foreground
    "fg-strong":          "#ffffff",
    "fg-normal":          "#dadada",
    "fg-weak":            "#969696",
    # Primary, secondary and accent colors
    "primary-strong":     "indigo-300",
    "primary-normal":     "indigo-500",
    "primary-weak":       "indigo-700",
    "secondary-strong":   "blue-grey-300",
    "secondary-normal":   "blue-grey-500",
    "secondary-weak":     "blue-grey-900",
    "accent1-strong":     "red-A100",
    "accent1-normal":     "red-A400",
    "accent1-weak":       "red-A700",
    "accent2-strong":     "amber-A100",
    "accent2-normal":     "amber-A400",
    "accent2-weak":       "amber-A700",
    # Semantic colors
    "semantic1":          "teal-400",
    "semantic2":          "brown-400",
    "semantic3":          "lime-400",
    "semantic4":          "light-green-400",
    "semantic5":          "grey-600",
    "semantic6":          "grey-800",
    "semantic7":          "purple-300",  # 400 is too dark
    "semantic8":          "blue-400",
    "semantic9":          "green-400",
    "semantic10":         "pink-400",
    "semantic11":         "cyan-400",
    # State colors
    "success-strong":     "green-200",
    "success-normal":     "green-400",
    "success-weak":       "#144517",
    "warning-strong":     "orange-200",
    "warning-normal":     "orange-400",
    "warning-weak":       "#994300",
    "error-strong":       "red-200",
    "error-normal":       "red-400",
    "error-weak":         "#851414",
    # ANSI colors
    "black":              "#121212",
    "red":                "red-400",
    "green":              "green-400",
    "yellow":             "lime-400",
    "blue":               "blue-400",
    "magenta":            "pink-400",
    "cyan":               "cyan-400",
    "white":              "#dadada",
    "dark-black":         "#000000",
    "dark-red":           "red-600",
    "dark-green":         "green-600",
    "dark-yellow":        "lime-600",
    "dark-blue":          "blue-600",
    "dark-magenta":       "pink-600",
    "dark-cyan":          "cyan-600",
    "dark-white":         "#969696",
    "bright-black":       "#1f1f1f",
    "bright-red":         "red-200",
    "bright-green":       "green-200",
    "bright-yellow":      "lime-200",
    "bright-blue":        "blue-200",
    "bright-magenta":     "pink-200",
    "bright-cyan":        "cyan-200",
    "bright-white":       "#ffffff",
}


theme = {
    # Views
    "view-bg":                    "bg-normal",
    "view-fg":                    "fg-normal",
    "view-header-bg":             "secondary-weak",
    "view-header-fg":             "primary-strong",
    "view-selected-bg":           "primary-weak",
    "view-selected-fg":           "fg-normal",
    "view-selected-inactive-bg":  "secondary-weak",
    "view-selected-inactive-fg":  "fg-normal",
    "view-marked-bg":             "bg-normal",
    "view-marked-fg":             "accent2-normal",
    "view-marked-inactive-bg":    "bg-normal",
    "view-marked-inactive-fg":    "accent2-weak",
    "view-highlighted-bg":        "accent1-normal",
    "view-highlighted-fg":        "bg-normal",
    "view-highlighted-inactive-bg": "accent2-normal",
    "view-highlighted-inactive-fg": "bg-normal",
    # Windows
    "window-bg":                  "bg-strong",
    "window-fg":                  "fg-normal",
    "window-title-active-bg":     "primary-normal",
    "window-title-active-fg":     "fg-strong",
    "window-title-inactive-bg":   "bg-strong",
    "window-title-inactive-fg":   "fg-weak",
    "window-title-urgent-bg":     "accent1-weak",
    "window-title-urgent-fg":     "fg-strong",
    "window-button-active-bg":    "primary-weak",
    "window-button-active-fg":    "fg-strong",
    "window-button-inactive-bg":  "bg-strong",
    "window-button-inactive-fg":  "fg-weak",
    "window-button-urgent-bg":    "accent1-normal",
    "window-button-urgent-fg":    "fg-strong",
    # Panels
    "panel-bg":                   "bg-strong",
    "panel-fg":                   "fg-normal",
    "panel-button-active-bg":     "primary-normal",
    "panel-button-active-fg":     "fg-strong",
    "panel-button-inactive-bg":   "bg-strong",
    "panel-button-inactive-fg":   "fg-weak",
    "panel-button-urgent-bg":     "accent1-normal",
    "panel-button-urgent-fg":     "fg-strong",
    # Menu
    "menu-bg":                    "secondary-weak",
    "menu-fg":                    "fg-normal",
    "menu-inactive-fg":           "fg-weak",
    "menu-selected-bg":           "primary-weak",
    "menu-selected-fg":           "fg-normal",
    # Tooltips
    "tooltip-bg":                 "fg-normal",
    "tooltip-fg":                 "bg-strong",
    # Scrollbars
    "scrollbar-bg":               "bg-strong",
    "scrollbar-fg":               "primary-weak",
    # Basic file types
    "file-broken-fg":             "accent1-normal",
    "file-directory-fg":          "fg-strong",
    "file-normal-fg":             "fg-normal",
    "file-link-fg":               "semantic4",
    "file-remote-fg":             "semantic4",  # Same as link
    "file-device-fg":             "semantic8",
    "file-special-fg":            "semantic2",
    "file-executable-fg":         "semantic3",
    "file-archive-fg":            "semantic7",
    "file-source-fg":             "semantic10",
    "file-document-fg":           "semantic1",
    "file-media-fg":              "semantic11",
    "file-temp-fg":               "semantic5",
    "file-readonly-fg":           "semantic9",
    "file-modified-fg":           "accent1-normal",
    # Basic source code elements
    "source-string-fg":           "semantic1",
    "source-doc-fg":              "semantic2",
    "source-function-fg":         "semantic3",
    "source-variable-fg":         "semantic4",
    "source-comment-fg":          "semantic5",
    "source-comment-delim-fg":    "semantic6",
    "source-builtin-fg":          "semantic11",
    "source-keyword-fg":          "semantic8",
    "source-preprocessor-fg":     "semantic7",
    "source-type-fg":             "semantic10",
    "source-constant-fg":         "semantic9",
    "source-warning-fg":          "warning-normal",
    "source-whitespace-bg":       "bg-strong",
    "source-whitespace-fg":       "semantic5",
    # Text
    "text-link-fg":               "semantic8",
    "text-tag-fg":                "semantic11",
    "text-section1-fg":           "semantic3",
    "text-section2-fg":           "semantic8",
    "text-section3-fg":           "semantic10",
    "text-section4-fg":           "semantic1",
    "text-section5-fg":           "semantic2",
    "text-section6-fg":           "semantic4",
    "text-section7-fg":           "semantic7",
    "text-section8-fg":           "semantic11",
    "text-section9-fg":           "semantic9",
    # Basic VC elements
    "vc-branch-fg":               "semantic1",
    "vc-tag-fg":                  "semantic4",
    "vc-sha-fg":                  "semantic10",
    # Cursor
    "cursor-normal-bg":           "accent2-normal",
    "cursor-read-only-bg":        "semantic9",
    "cursor-overwrite-bg":        "accent1-normal",
    "cursor-special-bg":          "semantic8",
    # Notification types
    "error-fg":                   "error-normal",
    "warning-fg":                 "warning-normal",
    "success-fg":                 "success-normal",
    # Diff
    "diff-add-fg":                "success-strong",
    "diff-add-bg":                "success-weak",
    "diff-delete-fg":             "error-strong",
    "diff-delete-bg":             "error-weak",
    "diff-change-fg":             "warning-strong",
    "diff-change-bg":             "warning-weak",
    "diff-context-fg":            "fg-weak",
    "diff-context-bg":            "bg-normal"
}
