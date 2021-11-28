'use strict';

function getScore(P1point, P2point) {
    var score = "";

    if (P1point === P2point && P1point < 3) {
        switch(P1point) {
            case 0:
                score = "Love"
                break
            case 1:
                score = "Fifteen"
                break
            case 2:
                score = "Thirty"
                break
            default:
        }
        score += "-All";
    }
    if (P1point === P2point && P1point > 2) {
        score = "Deuce";
    }

    var P1res;
    var P2res;
    if (P1point > 0 && P2point === 0) {
        switch(P1point) {
            case 1:
                P1res = "Fifteen"
                break
            case 2:
                P1res = "Thirty"
                break
            case 3:
                P1res = "Forty"
                break
            default:
        }

        P2res = "Love";
        score = P1res + "-" + P2res;
    }
    if (P2point > 0 && P1point === 0) {
        switch(P2point) {
            case 1:
                P2res = "Fifteen"
                break
            case 2:
                P2res = "Thirty"
                break
            case 3:
                P2res = "Forty"
                break
            default:
        }

        P1res = "Love";
        score = P1res + "-" + P2res;
    }

    if (P1point > P2point && P1point < 4) {
        switch(P1point) {
            case 2:
                P1res = "Thirty"
                break
            case 3:
                P1res = "Forty"
                break
            default:
        }
        switch(P2point) {
            case 1:
                P2res = "Fifteen"
                break
            case 2:
                P2res = "Thirty"
                break
            default:
        }
        score = P1res + "-" + P2res;
    }
    if (P2point > P1point && P2point < 4) {
        switch(P2point) {
            case 2:
                P2res = "Thirty"
                break
            case 3:
                P2res = "Forty"
                break
            default:
        }
        switch(P1point) {
            case 1:
                P1res = "Fifteen"
                break
            case 2:
                P1res = "Thirty"
                break
            default:
        }
        score = P1res + "-" + P2res;
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
