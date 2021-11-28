'use strict';

function getScore(P1point, P2point) {
    let score = ""
    let playerOneResult
    let playerTwoResult

    switch(P1point) {
        case 0:
            playerOneResult = "Love"
            break
        case 1:
            playerOneResult = "Fifteen"
            break
        case 2:
            playerOneResult = "Thirty"
            break
        case 3:
            playerOneResult = "Forty"
            break
        default:
    }

    switch(P2point) {
        case 0:
            playerTwoResult = "Love"
            break
        case 1:
            playerTwoResult = "Fifteen"
            break
        case 2:
            playerTwoResult = "Thirty"
            break
        case 3:
            playerTwoResult = "Forty"
            break
        default:
    }

    if (P1point === P2point && P1point < 3) {
        score += playerOneResult
        score += "-All";
    }
    if (P1point === P2point && P1point > 2) {
        score = "Deuce";
    }

    var P1res;
    var P2res;
    if (P1point > 0 && P2point === 0) {
        score = playerOneResult + "-" + playerTwoResult;
    }
    if (P2point > 0 && P1point === 0) {
        score = playerOneResult + "-" + playerTwoResult;
    }

    if (P1point > P2point && P1point < 4) {
        score = playerOneResult + "-" + playerTwoResult;
    }
    if (P2point > P1point && P2point < 4) {
        score = playerOneResult + "-" + playerTwoResult;
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
