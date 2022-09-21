import c4d
from c4d import gui
# Welcome to the world of Python


# Script state in the menu or the command palette
# Return True or c4d.CMD_ENABLED to enable, False or 0 to disable
# Alternatively return c4d.CMD_ENABLED|c4d.CMD_VALUE to enable and check/mark
#def state():
#    return True


#---------------------------
#Define variables
#---------------------------


# Main function



def main():
    def tool():
        return c4d.plugins.FindPlugin(doc.GetAction(), c4d.PLUGINTYPE_TOOL)

    def object():
        return doc.GetActiveObject()

    def tag():
        return doc.GetActiveTag()

    def renderdata():
        return doc.GetActiveRenderData()

    def prefs(id):
        return c4d.plugins.FindPlugin(id, c4d.PLUGINTYPE_PREFS)

    c4d.CallCommand(5159 # Create cube
    object()[c4d.PRIM_CUBE_LEN,c4d.VECTOR_X] = 200





# Execute main()
if __name__=='__main__':
    main()