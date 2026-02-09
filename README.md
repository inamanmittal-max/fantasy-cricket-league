## Fantasy Cricket League Backend

A Django-based backend system for a fantasy cricket league featuring
auction-based team creation, automated scoring, and dynamic leaderboards.


### Features
- Auction-based fantasy team creation with budget enforcement
- Rule-based points calculation from match performance
- Automated leaderboard updates using Django signals
- REST APIs exposed using Django REST Framework
- Admin panel for managing players, matches, and stats


### System Flow
1. Players are added to the system
2. Fantasy teams bid for players via auctions
3. Match stats are recorded per player
4. Points are calculated based on defined rules
5. Leaderboard updates automatically on stat changes


### Tech Stack
- Python
- Django
- Django REST Framework
-- SQLite (development)

 
 ### Run Locally
bash
git clone <repo-url>
cd cricket
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


