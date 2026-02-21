type User = { name: string; age: number };

function greet(u: User): string {
  return `Hello ${u.name}, you are ${u.age} years old.`;
}

const user: User = { name: "Yesh", age: 23 };
console.log(greet(user));
