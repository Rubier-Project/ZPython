source_list = []

class ImTierd(object):
    def addSource(source: str):
        source_list.append(source)
        return True

class CanyouReadMe(object):
    def getOutPut():
        if len(source_list) == 0:
            print("Please write a source")

        else:
            data = ""
            for src in source_list:
                data += f"{src}\n"

            try:
                exec(data)
            except Exception as ERR_EXEC:
                print(ERR_EXEC)
                pass

            data = ""
            source_list.clear()