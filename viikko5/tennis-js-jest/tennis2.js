'use strict';

function getScore(P1point, P2point) {
    let score = ""

    const results = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    let playerOneResult = results[P1point]
    let playerTwoResult = results[P2point]

    score = playerOneResult + "-" + playerTwoResult;

    if (P1point === P2point){
        switch(P1point < 3){
            case true:
                score = playerOneResult + "-All"
                break
            case false:
                score = "Deuce"
                break
            default:
        }
    }
    
    
    if (P1point > P2point && P2point >= 3) {
        score = "Advantage player1";
    }
    if (P2point > P1point && P1point >= 3) {
        score = "Advantage player2";
    }

    if (P1point >= 4 && P2point >= 0 && (P1point - P2point) >= 2) {
        score = "Win for player1";
    }
    if (P2point >= 4 && P1point >= 0 && (P2point - P1point) >= 2) {
        score = "Win for player2";
    }
    return score;
}

module.exports = getScore;
