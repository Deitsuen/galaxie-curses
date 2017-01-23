Constant Value
==============

enum BaselinePosition
---------------------
.. py:data:: BaselinePosition

   Whenever a container has some form of natural row it may align children in that row along a common typographical
   baseline. If the amount of vertical space in the row is taller than the total requested height of the
   baseline-aligned children then it can use a GtkBaselinePosition to select where to put the baseline inside the
   extra availible space.

      :glxc.BASELINE_POSITION_TOP: Align the baseline at the top
      :glxc.BASELINE_POSITION_CENTER: Center the baseline
      :glxc.BASELINE_POSITION_BOTTOM: Align the baseline at the bottom

enum DeleteType
---------------
.. py:data:: DeleteType

   See also: “delete-from-cursor”.

      :glxc.DELETE_CHARS: Delete characters.
      :glxc.DELETE_WORD_ENDS: Delete only the portion of the word to the left/right of cursor if we’re in the middle of a word.
      :glxc.DELETE_WORDS: Delete words.
      :glxc.DELETE_DISPLAY_LINES: Delete display-lines. Display-lines refers to the visible lines, with respect to to the current line breaks. As opposed to paragraphs, which are defined by line breaks in the input.
      :glxc.DELETE_DISPLAY_LINE_ENDS: Delete only the portion of the display-line to the left/right of cursor.
      :glxc.DELETE_PARAGRAPH_ENDS: Delete to the end of the paragraph. Like C-k in Emacs (or its reverse).
      :glxc.DELETE_PARAGRAPHS: Delete entire line. Like C-k in pico.
      :glxc.DELETE_WHITESPACE: Delete only whitespace. Like M-\ in Emacs.

enum DirectionType
------------------
.. py:data:: DirectionType

   Focus movement types.

      :glxc.DIR_TAB_FORWARD: Move forward.
      :glxc.DIR_TAB_BACKWARD: Move backward.
      :glxc.DIR_UP: Move up.
      :glxc.DIR_DOWN: Move down.
      :glxc.DIR_LEFT: Move left.
      :glxc.DIR_RIGHT: Move right.

enum Justification
------------------
.. py:data:: Justification

   Used for justifying the text inside a GtkLabel widget. (See also GtkAlignment).

      :glxc.JUSTIFY_LEFT: The text is placed at the left edge of the label.
      :glxc.JUSTIFY_RIGHT: The text is placed at the right edge of the label.
      :glxc.JUSTIFY_CENTER: The text is placed in the center of the label.
      :glxc.JUSTIFY_FILL: The text is placed is distributed across the label.

enum MovementStep
-----------------
.. py:data:: MovementStep

   Movements

      :glxc.MOVEMENT_LOGICAL_POSITIONS: Move forward or back by graphemes
      :glxc.MOVEMENT_VISUAL_POSITIONS: Move left or right by graphemes
      :glxc.MOVEMENT_WORDS: Move forward or back by words
      :glxc.MOVEMENT_DISPLAY_LINES: Move up or down lines (wrapped lines)
      :glxc.MOVEMENT_DISPLAY_LINE_ENDS: Move to either end of a line
      :glxc.MOVEMENT_PARAGRAPHS: Move up or down paragraphs (newline-ended lines)
      :glxc.MOVEMENT_PARAGRAPH_ENDS: Move to either end of a paragraph
      :glxc.MOVEMENT_PAGES: Move by pages
      :glxc.MOVEMENT_BUFFER_ENDS: Move to ends of the buffer
      :glxc.MOVEMENT_HORIZONTAL_PAGES: Move horizontally by pages

enum Orientation
----------------
.. py:data:: Orientation

   Represents the orientation of widgets and other objects which can be switched between horizontal and vertical orientation on the fly, like GtkToolbar or GtkGesturePan.

      :glxc.ORIENTATION_HORIZONTAL: The element is in horizontal orientation.
      :glxc.ORIENTATION_VERTICAL: The element is in vertical orientation.

enum PackType
-------------
.. py:data:: PackType

   Represents the packing location GtkBox children. (See: GtkVBox, GtkHBox, and GtkButtonBox).

      :glxc.PACK_START: The child is packed into the start of the box
      :glxc.PACK_END: The child is packed into the end of the box

enum PositionType
-----------------
.. py:data:: PositionType

   Describes which edge of a widget a certain feature is positioned at, e.g. the tabs of a GtkNotebook, the handle of a GtkHandleBox or the label of a GtkScale.

      :glxc.POS_LEFT: The feature is at the left edge.
      :glxc.POS_RIGHT: The feature is at the right edge.
      :glxc.POS_TOP: The feature is at the top edge.
      :glxc.POS_BOTTOM: The feature is at the bottom edge.

enum ReliefStyle
----------------
.. py:data:: ReliefStyle

   Indicated the relief to be drawn around a GtkButton.

      :glxc.RELIEF_NORMAL: Draw a normal relief.
      :glxc.RELIEF_HALF: A half relief. Deprecated in 3.14, does the same as glxc.RELIEF_NORMAL
      :glxc.RELIEF_NONE: No relief.

enum ScrollStep
---------------
.. py:data:: ScrollStep

   Type of relief

      :glxc.SCROLL_STEPS: Scroll in steps.
      :glxc.SCROLL_PAGES: Scroll by pages.
      :glxc.SCROLL_ENDS: Scroll to ends.
      :glxc.SCROLL_HORIZONTAL_STEPS: Scroll in horizontal steps.
      :glxc.SCROLL_HORIZONTAL_PAGES: Scroll by horizontal pages.
      :glxc.SCROLL_HORIZONTAL_ENDS: Scroll to the horizontal ends.

enum ScrollType
---------------
.. py:data:: ScrollStep

   Scrolling types.

      :glxc.SCROLL_NONE: No scrolling.
      :glxc.SCROLL_JUMP: Jump to new location.
      :glxc.SCROLL_STEP_BACKWARD: Step backward.
      :glxc.SCROLL_STEP_FORWARD: Step forward.
      :glxc.SCROLL_PAGE_BACKWARD: Page backward.
      :glxc.SCROLL_PAGE_FORWARD: Page forward.
      :glxc.SCROLL_STEP_UP: Step up.
      :glxc.SCROLL_STEP_DOWN: Step down.
      :glxc.SCROLL_PAGE_UP: Page up.
      :glxc.SCROLL_PAGE_DOWN: Page down.
      :glxc.SCROLL_STEP_LEFT: Step to the left.
      :glxc.SCROLL_STEP_RIGHT: Step to the right.
      :glxc.SCROLL_PAGE_LEFT: Page to the left.
      :glxc.SCROLL_PAGE_RIGHT: Page to the right.
      :glxc.SCROLL_START: Scroll to start.
      :glxc.SCROLL_END: Scroll to end.

enum SelectionMode
------------------
.. py:data:: SelectionMode

   Used to control what selections users are allowed to make.

      :glxc.SELECTION_NONE: No selection is possible.
      :glxc.SELECTION_SINGLE: Zero or one element may be selected.
      :glxc.SELECTION_BROWSE: Exactly one element is selected. In some circumstances, such as initially or during a search operation, it’s possible for no element to be selected with glxc.SELECTION_BROWSE. What is really enforced is that the user can’t deselect a currently selected element except by selecting another element.
      :glxc.SELECTION_MULTIPLE: Any number of elements may be selected. The Ctrl key may be used to enlarge the selection, and Shift key to select between the focus and the child pointed to. Some widgets may also allow Click-drag to select a range of elements.

enum ShadowType
---------------
.. py:data:: ShadowType

   Used to change the appearance of an outline typically provided by a GtkFrame.

   Note that many themes do not differentiate the appearance of the various shadow types: Either their is no visible shadow (glxc.SHADOW_NONE ), or there is (any other value).

      :glxc.SHADOW_NONE: No outline.
      :glxc.SHADOW_IN: The outline is bevelled inwards.
      :glxc.SHADOW_OUT: The outline is bevelled outwards like a button.
      :glxc.SHADOW_ETCHED_IN: The outline has a sunken 3d appearance.
      :glxc.SHADOW_ETCHED_OUT: The outline has a raised 3d appearance.

enum StateFlags
---------------
.. py:data:: StateFlags

   Describes a widget state. Widget states are used to match the widget against CSS pseudo-classes. Note that GTK extends the regular CSS classes and sometimes uses different names.

      :glxc.STATE_FLAG_NORMAL: State during normal operation.
      :glxc.STATE_FLAG_ACTIVE: Widget is active.
      :glxc.STATE_FLAG_PRELIGHT: Widget has a mouse pointer over it.
      :glxc.STATE_FLAG_SELECTED: Widget is selected.
      :glxc.STATE_FLAG_INSENSITIVE: Widget is insensitive.
      :glxc.STATE_FLAG_INCONSISTENT: Widget is inconsistent.
      :glxc.STATE_FLAG_FOCUSED: Widget has the keyboard focus.
      :glxc.STATE_FLAG_BACKDROP: Widget is in a background toplevel window.
      :glxc.STATE_FLAG_DIR_LTR: Widget is in left-to-right text direction. Since 3.8
      :glxc.STATE_FLAG_DIR_RTL: Widget is in right-to-left text direction. Since 3.8
      :glxc.STATE_FLAG_LINK: Widget is a link. Since 3.12
      :glxc.STATE_FLAG_VISITED: The location the widget points to has already been visited. Since 3.12
      :glxc.STATE_FLAG_CHECKED: Widget is checked. Since 3.14
      :glxc.STATE_FLAG_DROP_ACTIVE: Widget is highlighted as a drop target for DND. Since 3.20

enum ToolbarStyle
-----------------
.. py:data:: ToolbarStyle

   Used to customize the appearance of a GtkToolbar. Note that setting the toolbar style overrides the user’s preferences for the default toolbar style. Note that if the button has only a label set and glxc.TOOLBAR_ICONS is used, the label will be visible, and vice versa.

      :glxc.TOOLBAR_ICONS: Buttons display only icons in the toolbar.
      :glxc.TOOLBAR_TEXT: Buttons display only text labels in the toolbar.
      :glxc.TOOLBAR_BOTH: Buttons display text and icons in the toolbar.
      :glxc.TOOLBAR_BOTH_HORIZ: Buttons display icons and text alongside each other, rather than vertically stacked

enum SortType
-------------
.. py:data:: SortType

   Determines the direction of a sort.

      :glxc.SORT_ASCENDING: Sorting is in ascending order.
      :glxc.SORT_DESCENDING: Sorting is in descending order.
