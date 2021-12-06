'use strict';

function getScore(P1point, P2point) {
    let score = ""

    const results = {
        0: "Love",
        1: "Fifteen",
        2: "Thirty",
        3: "Forty"
    }

    //score = P1point === P2point && P1point < 3 ? results[P1point] + "-All" : "Deuce"

    if (P1point === P2point){
        switch(P1point < 3){
            case true:
                return results[P1point] + "-All"
            case false:
                return "Deuce"
            default:
        }
    }
    score = results[P1point] + "-" + results[P2point];
    
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
