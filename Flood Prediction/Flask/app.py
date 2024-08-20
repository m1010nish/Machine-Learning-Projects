from flask import Flask, request, jsonify, render_template
import numpy as np
import onnxruntime as ort

app = Flask(__name__)

# Load the ONNX model
sess = ort.InferenceSession("random_forest_model.onnx")

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.form.to_dict()
    input_data = [float(data[month]) for month in ['JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC', 'ANNUAL_RAINFALL']]
    input_data = np.array(input_data).reshape(1, -1).astype(np.float32)
    
    input_name = sess.get_inputs()[0].name
    label_name = sess.get_outputs()[0].name
    
    result = sess.run([label_name], {input_name: input_data})
    
    prediction = int(result[0][0])
    return jsonify({'With this rainfall quantity, Flood will Occur ? ': 'Yes' if prediction == 1 else 'No'})

if __name__ == '__main__':
    app.run(debug=True)
