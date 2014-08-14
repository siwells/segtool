import unittest

import segtool

class TestDescriptions(unittest.TestCase):

    def test_get_title(self):
        
        expected = ['Devoted Drivers', 'Image Improvers', 'Malcontented Motorists', 'Active Inspirers', 'Practical Travellers', 'Car Contemplators', 'PT Dependents', 'Car-Free Choosers']

        for x in range(1,9):
            out = segtool.get_segment_title(x)
            self.assertEqual(out, expected[x-1])

        expected = None
        out = segtool.get_segment_title(0)
        self.assertEqual(out, expected)

        out = segtool.get_segment_title(9)
        self.assertEqual(out, expected)

        
    def test_get_description(self):
        out = segtool.get_segment_description(1)
        expected = "You prefer to use a car than any other mode of transport and you are not interested in reducing your car use. You do not believe there are realistic alternatives to most of the journeys you make and you do not see yourself as a bus user or a cyclist anyway. Other modes are too slow and often stressful with few, if any, advantages over the car. It has probably been a while since you have been on a bus or a bike and you use a car most days. You tend to think successful people use cars and driving is a way to express yourself. You are not particularly motivated by using your travel time to get fit by using the bike or walking, and you are also not particularly motivated by reducing your emissions of greenhouse gases. You believe that people should be able to use their cars as much as they like with little restriction on this and you would like to see more roads built to reduce congestion."
        self.assertEqual(out, expected)

class TestHelper(unittest.TestCase):

    def test_get_segment(self):
        answers = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1],
            [5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5],
            [1,1,1,1,1,4,4,5,3,3,2,3,3,1,1,3,1]
            ]

        expected_true = ['3','3','3','2','2','3','2','3']
        expected_false = ['6','6','6','6','6','6','6','7']

        for x in range(len(answers)):
            out = segtool.get_segment(answers[x], True)
            self.assertEqual(out, expected_true[x])

        for x in range(len(answers)):
            out = segtool.get_segment(answers[x], False)
            self.assertEqual(out, expected_false[x])
            

class TestAllocation(unittest.TestCase):

    def test_allocate_segment(self):
        expected_true = ['3','3','3','2','2','3','2']
        expected_false = ['6','6','6','6','6','6','6']

        segments = [

            {'1': -34.24100000000001, '3': -25.258000000000003, '2': -36.23299999999999, 
            '5': -26.50099999999999, '4': -32.05499999999999, '7': -21.583999999999996, 
            '6': -20.789, '8': -24.995999999999995},

            {'1': 14.314999999999984, '3': 19.878, '2': 13.384000000000015, 
            '5': 17.286000000000016, '4': 13.637000000000015, '7': 13.735000000000007, 
            '6': 15.541999999999994, '8': 11.70300000000001},

            {'1': 62.87099999999998, '3': 65.01400000000001, '2': 63.001000000000005, 
            '5': 61.07299999999999, '4': 59.32899999999999, '7': 49.05400000000001, 
            '6': 51.873, '8': 48.401999999999994},

            {'1': 111.42699999999996, '3': 110.15, '2': 112.61800000000002, 
            '5': 104.86000000000003, '4': 105.02100000000003, 
            '7': 84.37300000000002, '6': 88.20399999999998, '8': 85.10100000000003},

            {'1': 159.98300000000003, '3': 155.28599999999997, '2': 162.23499999999999, 
            '5': 148.647, '4': 150.71300000000002, '7': 119.69200000000001, 
            '6': 124.535, '8': 121.80000000000001},
            
            {'1': 52.23800000000003, '3': 56.79900000000001, '2': 51.37000000000003, 
            '5': 49.17100000000001, '4': 49.69, '7': 48.54800000000001, 
            '6': 50.47800000000003, '8': 44.984},

            {'1': 73.50399999999999, '3': 73.22899999999998, '2': 74.63200000000003, 
            '5': 72.97499999999998, '4': 68.968, '7': 49.56000000000001, 
            '6': 53.26800000000001, '8': 51.820000000000014}

            ]

        for x in range(len(segments)):
            out = segtool.allocate_segment(segments[x], True)
            self.assertEqual(out, expected_true[x])

        for x in range(len(segments)):
            out  = segtool.allocate_segment(segments[x], False)
            self.assertEqual(out, expected_false[x])


class TestSegmentation(unittest.TestCase):

    def test_calculate_segment(self):
        expected = [

            {'1': -34.24100000000001, '3': -25.258000000000003, '2': -36.23299999999999, 
            '5': -26.50099999999999, '4': -32.05499999999999, '7': -21.583999999999996, 
            '6': -20.789, '8': -24.995999999999995},

            {'1': 14.314999999999984, '3': 19.878, '2': 13.384000000000015, 
            '5': 17.286000000000016, '4': 13.637000000000015, '7': 13.735000000000007, 
            '6': 15.541999999999994, '8': 11.70300000000001},

            {'1': 62.87099999999998, '3': 65.01400000000001, '2': 63.001000000000005, 
            '5': 61.07299999999999, '4': 59.32899999999999, '7': 49.05400000000001, 
            '6': 51.873, '8': 48.401999999999994},

            {'1': 111.42699999999996, '3': 110.15, '2': 112.61800000000002, 
            '5': 104.86000000000003, '4': 105.02100000000003, 
            '7': 84.37300000000002, '6': 88.20399999999998, '8': 85.10100000000003},

            {'1': 159.98300000000003, '3': 155.28599999999997, '2': 162.23499999999999, 
            '5': 148.647, '4': 150.71300000000002, '7': 119.69200000000001, 
            '6': 124.535, '8': 121.80000000000001},
            
            {'1': 52.23800000000003, '3': 56.79900000000001, '2': 51.37000000000003, 
            '5': 49.17100000000001, '4': 49.69, '7': 48.54800000000001, 
            '6': 50.47800000000003, '8': 44.984},

            {'1': 73.50399999999999, '3': 73.22899999999998, '2': 74.63200000000003, 
            '5': 72.97499999999998, '4': 68.968, '7': 49.56000000000001, 
            '6': 53.26800000000001, '8': 51.820000000000014}

            ]
        answers = [
            [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
            [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
            [3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
            [4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4],
            [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
            [1,2,3,4,5,4,3,2,1,2,3,4,5,4,3,2,1],
            [5,4,3,2,1,2,3,4,5,4,3,2,1,2,3,4,5]
            ]

        for x in range(len(answers)):
            out = segtool.calculate_segment(answers[x])
            
#            tmp = expected[x]

            for y in range(1,9):
                y = str(y)
                self.assertEqual(out[y], expected[x][y])
            

if __name__ == "__main__":
    
    unittest.main()
