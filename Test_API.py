import unittest
import requests


class TestAPI(unittest.TestCase):
    URL="http://172.17.0.3:5000/Guess_Name_RF"

    def get_prediction_Fake(self):
        data={'text': 'اكابرم حسسني محمد'}
        expected_result={"Name": "اكابرم حسسني محمد", "Prediction": "Model classify it as  Fake Name", "probability": 0.82, "Inference_time": "time is 0.009717226028442383 ms"}
        response=requests.post(url=self.URL,json=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()),4)
        res=response.json()
        self.assertEqual(res['Prediction'],expected_result['Prediction'])
        print("test1 Completed")

    def get_prediction_Correct(self):
        data={"text": "مهند عبدالحليم ابراهيم"}
        expected_result={"Name": "مهند عبدالحليم ابراهيم", "Prediction": "Model classify it as  Correct Name", "probability": 1.0, "Inference_time": "time is 0.009463787078857422 ms"}
        response=requests.post(url=self.URL,json=data)
        self.assertEqual(response.status_code,200)
        self.assertEqual(len(response.json()),4)
        res=response.json()
        self.assertEqual(res['Prediction'],expected_result['Prediction'])
        print("test2 Completed")





if __name__=='__main__':

    test=TestAPI()
    test.get_prediction_Fake()
    test.get_prediction_Correct()
