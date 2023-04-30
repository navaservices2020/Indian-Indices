CREATE TABLE transactions (
  transaction_id INT NOT NULL PRIMARY KEY,
  transaction_date TIMESTAMP NOT NULL,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL
);


CREATE TABLE stock_transactions (
  transaction_id INT NOT NULL PRIMARY KEY,
  transaction_date TIMESTAMP NOT NULL,
  stock_symbol VARCHAR(10) NOT NULL,
  buyer_id INT NOT NULL,
  seller_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  total DECIMAL(10, 2) NOT NULL
);


CREATE TABLE transactions (
  transaction_id INT NOT NULL PRIMARY KEY,
  transaction_date DATE NOT NULL,
  customer_id INT NOT NULL,
  product_id INT NOT NULL,
  quantity INT NOT NULL,
  price DECIMAL(10, 2) NOT NULL,
  total DECIMAL(10, 2) NOT NULL,
  payment_method VARCHAR(50) NOT NULL
);

CREATE TABLE bank_transactions (
  transaction_id INT NOT NULL PRIMARY KEY,
  transaction_date TIMESTAMP NOT NULL,
  account_number VARCHAR(50) NOT NULL,
  transaction_type VARCHAR(50) NOT NULL,
  amount DECIMAL(10, 2) NOT NULL,
  balance DECIMAL(10, 2) NOT NULL
);

CREATE TABLE cricket_batsman_stats (
  player_id INT NOT NULL PRIMARY KEY,
  player_name VARCHAR(50) NOT NULL,
  matches_played INT NOT NULL,
  innings_played INT NOT NULL,
  runs_scored INT NOT NULL,
  balls_faced INT NOT NULL,
  highest_score INT NOT NULL,
  batting_average DECIMAL(5, 2) NOT NULL,
  strike_rate DECIMAL(5, 2) NOT NULL,
  centuries INT NOT NULL,
  half_centuries INT NOT NULL,
  fours INT NOT NULL,
  sixes INT NOT NULL
);


CREATE TABLE cricket_bowler_stats (
  player_id INT NOT NULL PRIMARY KEY,
  player_name VARCHAR(50) NOT NULL,
  matches_played INT NOT NULL,
  innings_bowled INT NOT NULL,
  balls_bowled INT NOT NULL,
  runs_conceded INT NOT NULL,
  wickets INT NOT NULL,
  best_bowling_figure VARCHAR(10) NOT NULL,
  bowling_average DECIMAL(5, 2) NOT NULL,
  economy DECIMAL(5, 2) NOT NULL,
  strike_rate DECIMAL(5, 2) NOT NULL,
  five_wicket_hauls INT NOT NULL
);

CREATE TABLE cricket_match (
  match_id INT NOT NULL PRIMARY KEY,
  match_type VARCHAR(20) NOT NULL,
  venue VARCHAR(50) NOT NULL,
  match_date DATE NOT NULL,
  team1_id INT NOT NULL,
  team2_id INT NOT NULL,
  result VARCHAR(20) NOT NULL,
  winner_id INT,
  man_of_the_match_id INT,
  umpire1_id INT,
  umpire2_id INT,
  FOREIGN KEY (team1_id) REFERENCES cricket_team (team_id),
  FOREIGN KEY (team2_id) REFERENCES cricket_team (team_id),
  FOREIGN KEY (winner_id) REFERENCES cricket_team (team_id),
  FOREIGN KEY (man_of_the_match_id) REFERENCES cricket_player (player_id),
  FOREIGN KEY (umpire1_id) REFERENCES cricket_umpire (umpire_id),
  FOREIGN KEY (umpire2_id) REFERENCES cricket_umpire (umpire_id)
);