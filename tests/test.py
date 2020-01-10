from main import Canvas


class CanvasTest:

    @staticmethod
    def test1():
        can = Canvas()
        can.execute_сommands("test01_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test01_expected.txt")

    @staticmethod
    def test2():
        can = Canvas()
        can.execute_сommands("test02_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test02_expected.txt")

    @staticmethod
    def test3():
        can = Canvas()
        can.execute_сommands("test03_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test03_expected.txt")

    @staticmethod
    def test4():
        can = Canvas()
        can.execute_сommands("test04_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test04_expected.txt")

    @staticmethod
    def test5():
        can = Canvas()
        can.execute_сommands("test05_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test05_expected.txt")

    @staticmethod
    def test6():
        can = Canvas()
        can.execute_сommands("test06_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test06_expected.txt")

    @staticmethod
    def test7():
        can = Canvas()
        can.execute_сommands("test07_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test07_expected.txt")

    @staticmethod
    def test8():
        can = Canvas()
        can.execute_сommands("test08_input_command.txt")
        can.writeInFile("test_actual.txt")

        CanvasTest.assertCanvas("test_actual.txt", "test08_expected.txt")


    @staticmethod
    def assertCanvas(result_file_name: str, accepted_file_name: str):
        result = []
        accepted = []

        for j in open(result_file_name).readlines():
            result.append(j)

        for i in open(accepted_file_name).readlines():
            accepted.append(i)

        if len(result) == len(accepted):
            res = True
            for index in range(len(result)):
                res = res and (result[index] == accepted[index])
        else:
            res = False

        assert res


CanvasTest.test1()
CanvasTest.test2()
CanvasTest.test3()
CanvasTest.test4()
CanvasTest.test5()
CanvasTest.test6()
CanvasTest.test7()
CanvasTest.test8()

