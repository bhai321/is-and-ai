function isPrime(n) {
    if (n < 2) return false;
    for (let i = 2; i <= Math.sqrt(n); i++) {
    if (n % i === 0) return false;
    }
    return true;
    }
    function generateKeys() {
    const prime = parseInt(document.getElementById("prime").value);
    const base = parseInt(document.getElementById("base").value);
    if (!isPrime(prime)) {
    alert("Please enter a prime number.");
    return;
    }
    const alicePrivateKey = Math.floor(Math.random() * (prime - 2)) + 2;
    const bobPrivateKey = Math.floor(Math.random() * (prime - 2)) + 2;
    const alicePublicKey = modExp(base, alicePrivateKey, prime);
    const bobPublicKey = modExp(base, bobPrivateKey, prime);
    const sharedSecret = modExp(alicePublicKey, bobPrivateKey, prime);
    document.getElementById("alicePubKey").textContent = alicePublicKey;
    document.getElementById("bobPubKey").textContent = bobPublicKey;
    document.getElementById("sharedSecret").textContent = sharedSecret;
    }
    function modExp(base, exponent, modulus) {
    if (modulus === 1) return 0;
    let result = 1;
    base = base % modulus;
    while (exponent > 0) {
    if (exponent % 2 === 1) {
    result = (result * base) % modulus;
    }
    exponent = Math.floor(exponent / 2);
    base = (base * base) % modulus;
    }
    return result;
    }