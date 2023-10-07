let
	items,
	createNewItem,
	
	openOrders,
	closedOrders
;

window.addEventListener("load", () => {
	
	items = document.querySelector("#Items > tbody");
	loadItems();
	
	createNewItem = document.querySelector("#createNewItem");
	createNewItem.addEventListener("click", e => {
		document.querySelector("#AddItem").classList.toggle("hide");
		e.preventDefault();
	});
	
	openOrders = document.querySelector("#open-orders tbody");
	closedOrders = document.querySelector("#past-orders tbody");
	loadOrders();
	
	document.querySelector("#AddNewItem").addEventListener("click", addItem);
});

async function loadItems(){
	let r = await sendApiRequest("/farmer/products");
	let data = await r.json();
	
	if(r.status != 200)
		console.error(data);
	
	for(let p of data.products)
		items.appendChild(createItemRow(p));
}

function createItemRow(p){
	let tr = createElement("tr");
	
	for(let e of [
			p.category,
			p.item,
			p.totalQty + " " + p.unit,
			p.availableQty + " " + p.unit,
			"₹ " + p.price
		])
		createElement("td", tr, {innerText: e});
	
	let removeButton = createElement("td", tr);
	createElement("i.fa.fa-minus-circle", removeButton);
	removeButton.addEventListener("click", removeItem);
	
	return tr;
}

async function removeItem(e){
	await sendApiRequest("/farmer/product", {
		method: "DELETE",
		body: {
			item: this.parentElement.querySelector("td:nth-child(2)").innerText
		}
	}).then(assertOK);
	
	this.parentElement.remove();
}

async function addItem(){
	let data = {
		category: document.querySelector("#Item").selectedOptions[0].parentElement.label,
		item: document.querySelector("#Item").selectedOptions[0].value,
		unit: document.querySelector("#Unit").selectedOptions[0].value,
		totalQty: +document.querySelector("#Quantity").value,
		availableQty: +document.querySelector("#Quantity").value,
		price: +document.querySelector("#Price").value,
	};
	
	await sendApiRequest("/farmer/product/add", {
		method: "POST",
		body: data
	}).then(assertOK);
	items.appendChild(createItemRow(data));
	
	document.querySelector("#AddItem").classList.add("hide");
	document.querySelector("#Quantity").value = "";
	document.querySelector("#Price").value = "";
}

async function loadOrders(){
	let data = await sendApiRequest("/wholesaler/orders")
		.then(assertOK)
		.then(e => e.json());
	
	for(let o of data.orders)
		addOrderRow(o);
}

function addOrderRow(p){
	let tr = createElement("tr");
	
	let d = new Date(p.date);
	let date = 
		(d.getDate()) + "/" +
		(d.getMonth() + 1) + "/" +
		(d.getYear() + 1900)
	;
	
	for(let e of [
			date,
			p.product.category,
			p.product.item,
			p.quantity + " " + p.product.unit,
			"₹ " + p.product.price,
			p.wholesalerId
		])
		createElement("td", tr, {innerText: e});
	
	if(p.isOpen)
		openOrders.appendChild(tr);
	else
		closedOrders.appendChild(tr);
	
	return tr;
}