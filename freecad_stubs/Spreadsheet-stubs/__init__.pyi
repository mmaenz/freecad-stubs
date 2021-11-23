import FreeCAD
import Spreadsheet


# SheetPy.xml
class Sheet(FreeCAD.DocumentObject):
    """With this object you can manipulate spreadsheets"""

    @property
    def cells(self) -> Spreadsheet.Sheet:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertySheet.
        Cell contents.
        """

    @property
    def columnWidths(self) -> Spreadsheet.PropertyColumnWidths:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertyColumnWidths.
        Column widths.
        """

    @property
    def docDeps(self) -> list[FreeCAD.DocumentObject | None]:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Transient] Property content won't be saved to file, but still saves name, type and status.
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Spreadsheet.
        Property TypeId: App::PropertyLinkList.
        Dependencies.
        """

    @property
    def rowHeights(self) -> Spreadsheet.PropertyRowHeights:
        """
        [Prop_ReadOnly] Property is read-only in the editor.
        [Prop_Hidden] Property won't appear in the editor.
        Property group: Spreadsheet.
        Property TypeId: Spreadsheet::PropertyRowHeights.
        Row heights.
        """

    def clear(self, arg1: str, arg2: bool = None, /):
        """
        Clear a cell
        Possible exceptions: (ValueError).
        """

    def clearAll(self):
        """Clear all cells in the spreadsheet"""

    def exportFile(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, /) -> bool:
        """Export file from spreadsheet"""

    def get(self, arg1: str, /) -> FreeCAD.Property:
        """
        Get evaluated cell contents
        Possible exceptions: (ValueError).
        """

    def getAlias(self, arg1: str, /) -> str | None:
        """
        Get alias for cell address
        Possible exceptions: (ValueError).
        """

    def getAlignment(self, arg1: str, /) -> object | None:
        """
        Get alignment of the cell
        Possible exceptions: (ValueError).
        """

    def getBackground(self, arg1: str, /) -> tuple[float, float, float, float] | None:
        """
        Get background color of the cell
        Possible exceptions: (ValueError).
        """

    def getCellFromAlias(self, arg1: str, /) -> str | None:
        """
        Get cell address given an alias
        Possible exceptions: (ValueError).
        """

    def getColumnWidth(self, arg1: str, /) -> int:
        """
        Get given spreadsheet column width
        Possible exceptions: (ValueError).
        """

    def getContents(self, arg1: str, /) -> str:
        """
        Get cell contents
        Possible exceptions: (ValueError).
        """

    def getDisplayUnit(self, arg1: str, /) -> str:
        """
        Get display unit for cell
        Possible exceptions: (ValueError).
        """

    def getForeground(self, arg1: str, /) -> tuple[float, float, float, float] | None:
        """
        Get foreground color of the cell
        Possible exceptions: (ValueError).
        """

    def getRowHeight(self, arg1: str, /) -> int:
        """
        Get given spreadsheet row height
        Possible exceptions: (ValueError).
        """

    def getStyle(self, arg1: str, /) -> object | None:
        """
        Get style of the cell
        Possible exceptions: (ValueError).
        """

    def importFile(self, arg1: str, arg2: str = None, arg3: str = None, arg4: str = None, /) -> bool:
        """Import file into spreadsheet"""

    def insertColumns(self, arg1: str, arg2: int, /):
        """Insert a given number of columns into the spreadsheet."""

    def insertRows(self, arg1: str, arg2: int, /):
        """Insert a given number of rows into the spreadsheet."""

    def mergeCells(self, arg1: str, /):
        """Merge given cell area into one cell"""

    def removeColumns(self, arg1: str, arg2: int, /):
        """Remove a given number of columns from the spreadsheet."""

    def removeRows(self, arg1: str, arg2: int, /):
        """Remove a given number of rows from the spreadsheet."""

    def set(self, arg1: str, arg2: str, /):
        """
        Set data into a cell
        Possible exceptions: (ValueError).
        """

    def setAlias(self, arg1: str, arg2, /):
        """
        Set alias for cell address
        Possible exceptions: (ValueError).
        """

    def setAlignment(self, arg1: str, arg2, arg3: str = None, /):
        """
        Set alignment of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def setBackground(self, arg1: str, arg2, /):
        """
        Set background color of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def setColumnWidth(self, arg1: str, arg2: int, /):
        """
        Set given spreadsheet column to given width
        Possible exceptions: (ValueError).
        """

    def setDisplayUnit(self, arg1: str, arg2: str, /):
        """
        Set display unit for cell
        Possible exceptions: (ValueError).
        """

    def setForeground(self, arg1: str, arg2, /):
        """
        Set foreground color of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def setRowHeight(self, arg1: str, arg2: int, /):
        """
        Set given spreadsheet row to given height
        Possible exceptions: (ValueError).
        """

    def setStyle(self, arg1: str, arg2, arg3: str = None, /):
        """
        Set style of the cell
        Possible exceptions: (TypeError, ValueError).
        """

    def splitCell(self, arg1: str, /):
        """
        Split a previously merged cell
        Possible exceptions: (ValueError).
        """
