from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from models import Game, Review

if __name__ == '__main__':
    engine = create_engine('sqlite:///one_to_many.db')
    Session = sessionmaker(bind=engine)
    session = Session()

# Access the first review instance in the database
    def get_one_review():
        return session.query(Review).first()

    # Find a specific game instance using an ID
    def get_game_by_id(game_id):
        return session.query(Game).filter_by(id=Review.game_id).first()

    #access the first game
    def get_first_game():
        return session.query(Game).first()