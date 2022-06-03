pragma solidity ^0.5.0;

//  Import the following contracts from the OpenZeppelin library:
//    * `ERC20`
//    * `ERC20Detailed`
//    * `ERC20Mintable`
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Detailed.sol";
import "https://github.com/OpenZeppelin/openzeppelin-contracts/blob/release-v2.5.0/contracts/token/ERC20/ERC20Mintable.sol";

// Create a constructor for the RewardsRTokens contract and have the contract inherit the
// libraries that you imported from OpenZeppelin.

contract RewardsRTokens is ERC20, ERC20Detailed, ERC20Mintable {

    constructor(string memory name, string memory symbol, uint initial_supply)
        ERC20Detailed(name, symbol, 18) public {
            // constructor can stay empty
        }

    address payable accountOne;
    address payable accountTwo;
    address payable accountThree;
    address payable accountFour;
    address payable accountFive;
    address payable accountSix;
    address payable accountSeven;
    address payable accountEight;
    address payable accountNine;
    address payable accountTen;
    address public lastToWithdraw;
    uint public lastWithdrawAmount;
    uint public contractBalance;

    function redeem(uint amount, address payable recipient) public{
        require(amount <= contractBalance, "You don't have enough funds!");

        // Call the `transfer` function of the `recipient` and pass it the `amount` to transfer as an argument.
        recipient.transfer(amount);

        // Set  `lastWithdrawAmount` equal to `amount`
        lastWithdrawAmount = amount;

        // Call the `contractBalance` variable and set it equal to the balance of the contract by 
        // using `address(this).balance` to reflect the new balance of the contract.
        contractBalance = address(this).balance;


    }

    // Define a `public payable` function named `deposit`.
    function deposit() public payable {
        contractBalance = address(this).balance;

    }

    // Fallback function
    function() external payable{}

}