from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
db = SQLAlchemy(app)
""" Another way to run the app"""

from src import create_app

app = create_app()

if __name__ == "__main__":
    app.run()

from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from flask_bcrypt import Bcrypt
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///development.db')
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'super-secret')  # Change this!
db = SQLAlchemy(app)
jwt = JWTManager(app)
bcrypt = Bcrypt(app)

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        additional_claims = {"is_admin": user.is_admin}
        access_token = create_access_token(identity=user.id, additional_claims=additional_claims)
        return jsonify(access_token=access_token), 200
    return 'Wrong email or password', 401

@app.route('/admin/data', methods=['POST', 'DELETE'])
@jwt_required()
def admin_data():
    claims = get_jwt()
    if not claims.get('is_admin'):
        return jsonify({"msg": "Administration rights required"}), 403
    # Proceed with admin-only functionality
