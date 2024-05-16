/* eslint-disable */
import Currency from './3-currency.js';

export default class Pricing {
	constructor(amount, currency){
	  this.__amount = amount;
	  this.__currency = currency;
	}
	
	displayFullPrice(){
		return (`${this.amount} ${this.currency.name} (${this.currency.code})`);
	}

	static convertPrice(amount, conversionRate) {
		return amount * conversionRate;
	}

	set amount(newAmount) {
    		this._amount = newAmount;
  	}

  	set currency(currency) {
    		this._currency = currency;
  	}

  	get amount() {
    		return this._amount;
  	}

 	get currency() {
	  	return this._currency;
	}
}
