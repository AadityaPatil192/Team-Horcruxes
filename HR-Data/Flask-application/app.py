from flask import Flask, request, render_template, jsonify
from flask_pymongo import PyMongo

app = Flask(__name__)

# MongoDB configuration
app.config["MONGO_URI"] = "mongodb+srv://aadityapatil1902:root@cluster0.wvbc0gp.mongodb.net/hr-data"
mongo = PyMongo(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_candidate', methods=['POST'])
def get_candidate():
    try:
        # Convert Candidate_Ref from the form to an integer
        Candidate_Ref = int(request.form['Candidate_Ref'])
        print(f"Received candidate reference: {Candidate_Ref}")  # Debug statement

        # Using PyMongo to find one document
        candidate = mongo.db.details.find_one({'Candidate_Ref': Candidate_Ref})
        print(f"Candidate found: {candidate}")  # Debug statement
        print(f"Type of candidate: {type(candidate)}")  # Debug statement

        if candidate:
            candidate.pop('_id', None)  # Optionally remove the _id field if not needed
            candidate.pop('Sno', None)
            return jsonify(candidate)
        else:
            print("Candidate not found")  # Debug statement
            return jsonify({'error': 'Candidate not found'}), 404
    except ValueError:
        print("Invalid input for Candidate_Ref, must be an integer")  # Debug for non-integer input
        return jsonify({'error': 'Invalid input, Candidate_Ref must be an integer'}), 400
    except Exception as e:
        print(f"Error occurred: {e}")  # Debug statement
        return jsonify({'error': f'An error occurred while fetching candidate data: {e}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
