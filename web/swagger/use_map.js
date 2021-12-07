const Decimal = require('decimal.js');

let lst = [
    { value: null },
    { value: null },
    { value: null },
    { value: null },
]


lst = lst.map((plan, index) => {
    console.log(index);
    if (index < lst.length - 1) {
        plan.value = new Decimal(100);
        return plan;
    }
    plan.value = new Decimal(99);
    return plan
})
console.log(lst)
