import unittest
def suma(num_1,num_2):
    pass


class CajaNegratest(unittest.TestCase):

    def test_suma_dos_positivos(self):
        num_1=10
        num_2=5

        resultado= suma(num_1,num_2)

        self.assertEqual(resultado,15)

if __name__=='__main':
    unittest.main()
