//SPDX-License-Identifier: MIT

pragma solidity ^0.8.7;

import "@chainlink/contracts/src/v0.8/interfaces/AggregatorV3Interface.sol";

//https://ethereum.stackexchange.com/questions/99677/how-can-msg-sender-addressthis
//https://medium.com/swlh/getting-deep-into-evm-how-ethereum-works-backstage-ab6ad9c0d0bf
//https://betterprogramming.pub/learn-solidity-functions-ddd8ea24c00d

contract Fundme {
    uint256 public don;
    address public owner;
    AggregatorV3Interface public newprice;

    constructor(address pricefeed) {
        newprice = AggregatorV3Interface(pricefeed);
        owner = address(this);
    }

    function fund() public payable {
        uint256 donate = (msg.value * price()) / (10**8);
        don = donate;
    }

    function getversion() public view returns (uint256) {
        return newprice.version();
    }

    function price() public view returns (uint256) {
        (, int256 ans, , , ) = newprice.latestRoundData();
        return uint256(ans);
    }

    function withdraw() public payable {
        payable(msg.sender).transfer(address(this).balance);
    }

    function checkbalance() public view returns (uint256) {
        return address(this).balance;
    }
}
