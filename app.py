import os
from dotenv import load_dotenv
from groq import Groq
import json
from pydantic import BaseModel
import webbrowser

load_dotenv()

client = Groq(
    api_key = os.getenv("GROQ_API_KEY"),
)

class Code(BaseModel):
    html_code : str

def html_code_generator(info: str) -> Code:
    chat_completion = client.chat.completions.create(
        messages = [
            {
                "role" : "system",
                "content" : "You are a react to HTML converter. You have to convert the given react code to HTML code.Include inline CSS code in the HTML code.\n"
                f" The JSON object must use the schema: {json.dumps(Code.model_json_schema(), indent=2)}",
            },
            {
                "role" : "user",
                "content" : f"the react code : {info}",
            },
        ],
        model = "llama-3.3-70b-versatile",
        temperature = 0,
        stream = False,
        response_format = {"type": "json_object"},
    )
    return Code.model_validate_json(chat_completion.choices[0].message.content)

react_code = '''
import React, { useState } from 'react';

const App = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="min-h-screen flex flex-col justify-center">
      <Navbar setIsOpen={setIsOpen} />
      <HeroSection />
      <main className="container mx-auto p-4 pt-6 md:p-6 lg:p-12">
        <ProductList products={[
          { id: 1, title: 'Product 1', description: 'Description 1', price: 10.99, image: 'https://picsum.photos/200/300' },
          { id: 2, title: 'Product 2', description: 'Description 2', price: 9.99, image: 'https://picsum.photos/200/301' },
          { id: 3, title: 'Product 3', description: 'Description 3', price: 12.99, image: 'https://picsum.photos/200/302' },
        ]} />
        <ProductDetail product={{
          id: 1,
          title: 'Product 1',
          description: 'Description 1',
          price: 10.99,
          image: 'https://picsum.photos/200/300',
          features: [
            { id: 1, name: 'Feature 1' },
            { id: 2, name: 'Feature 2' },
          ],
          reviews: [
            { id: 1, text: 'Review 1' },
            { id: 2, text: 'Review 2' },
          ],
        }} />
        <ContactForm />
        <SellYourGoodsForm />
      </main>
      <Footer />
    </div>
  );
};

const Navbar = ({ setIsOpen }) => {
  return (
    <nav className="fixed top-0 left-0 w-full h-16 bg-gradient-to-r from-gray-800 to-gray-900 text-white flex justify-between items-center py-4 px-6">
      <div className="flex justify-between items-center w-full">
        <a href="#" className="text-lg font-bold">
          Logo
        </a>
        <button
          className="lg:hidden flex justify-center w-8 h-8 bg-gray-200 hover:bg-gray-300 rounded-full focus:outline-none"
          onClick={() => setIsOpen(!isOpen)}
        >
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <rect x="4" y="5" width="8" height="8" rx="1" fill="#fff" />
            <rect x="12" y="5" width="8" height="8" rx="1" fill="#fff" />
            <rect x="4" y="13" width="8" height="8" rx="1" fill="#fff" />
            <rect x="12" y="13" width="8" height="8" rx="1" fill="#fff" />
          </svg>
        </button>
      </div>
      <ul
        className={`lg:flex justify-between items-center w-full absolute lg:static top-16 lg:w-auto lg:left-0 lg:right-0 lg:bg-transparent lg:shadow-none z-50 ${
          isOpen ? 'block' : 'hidden'
        }`}
      >
        <li>
          <a href="#" className="block py-2 px-4 hover:bg-gray-200">
            Home
          </a>
        </li>
        <li>
          <a href="#" className="block py-2 px-4 hover:bg-gray-200">
            Products
          </a>
        </li>
        <li>
          <a href="#" className="block py-2 px-4 hover:bg-gray-200">
            About
          </a>
        </li>
        <li>
          <a href="#" className="block py-2 px-4 hover:bg-gray-200">
            Contact
          </a>
        </li>
      </ul>
    </nav>
  );
};

const HeroSection = () => {
  return (
    <section className="h-screen flex justify-center items-center bg-cover bg-center" style={{ backgroundImage: 'url(https://picsum.photos/2000/1000)' }}>
      <div className="container mx-auto p-4 pt-6 md:p-6 lg:p-12">
        <h1 className="text-4xl font-bold text-white mb-4">Welcome to our e-commerce website!</h1>
        <p className="text-lg text-white mb-8">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sit amet nulla auctor, vestibulum magna sed, convallis ex.</p>
        <button className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded">
          Shop Now
        </button>
      </div>
    </section>
  );
};

const ProductCard = ({ product }) => {
  return (
    <div className="max-w-sm rounded overflow-hidden shadow-lg">
      <img src={product.image} alt={product.title} className="w-full h-48 object-cover" />
      <div className="px-6 py-4">
        <h2 className="font-bold text-lg">{product.title}</h2>
        <p className="text-gray-700">{product.description}</p>
        <p className="text-gray-700">${product.price}</p>
      </div>
      <button className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded">
        Add to Cart
      </button>
    </div>
  );
};

const ProductList = ({ products }) => {
  return (
    <div className="container mx-auto p-4 pt-6 md:p-6 lg:p-12">
      <h2 className="text-2xl font-bold mb-4">Products</h2>
      <ul className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {products.map((product) => (
          <li key={product.id}>
            <ProductCard product={product} />
          </li>
        ))}
      </ul>
    </div>
  );
};

const ProductDetail = ({ product }) => {
  return (
    <div className="container mx-auto p-4 pt-6 md:p-6 lg:p-12">
      <h2 className="text-2xl font-bold mb-4">{product.title}</h2>
      <img src={product.image} alt={product.title} className="w-full h-48 object-cover mb-4" />
      <p className="text-gray-700">{product.description}</p>
      <h3 className="text-lg font-bold mb-4">Features</h3>
      <ul>
        {product.features.map((feature) => (
          <li key={feature.id}>{feature.name}</li>
        ))}
      </ul>
      <h3 className="text-lg font-bold mb-4">Reviews</h3>
      <ul>
        {product.reviews.map((review) => (
          <li key={review.id}>{review.text}</li>
        ))}
      </ul>
      <button className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded">
        Add to Cart
      </button>
    </div>
  );
};

const ContactForm = () => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [message, setMessage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', { name, email, message });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 pt-6 md:p-6 lg:p-12">
      <h2 className="text-2xl font-bold mb-4">Contact Us</h2>
      <label className="block mb-2">
        Name
        <input type="text" value={name} onChange={(e) => setName(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <label className="block mb-2">
        Email
        <input type="email" value={email} onChange={(e) => setEmail(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <label className="block mb-2">
        Message
        <textarea value={message} onChange={(e) => setMessage(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <button type="submit" className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded">
        Send
      </button>
    </form>
  );
};

const SellYourGoodsForm = () => {
  const [title, setTitle] = useState('');
  const [description, setDescription] = useState('');
  const [price, setPrice] = useState('');
  const [image, setImage] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    console.log('Form submitted:', { title, description, price, image });
  };

  return (
    <form onSubmit={handleSubmit} className="max-w-md mx-auto p-4 pt-6 md:p-6 lg:p-12">
      <h2 className="text-2xl font-bold mb-4">Sell Your Goods</h2>
      <label className="block mb-2">
        Title
        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <label className="block mb-2">
        Description
        <textarea value={description} onChange={(e) => setDescription(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <label className="block mb-2">
        Price
        <input type="number" value={price} onChange={(e) => setPrice(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <label className="block mb-2">
        Image
        <input type="file" value={image} onChange={(e) => setImage(e.target.value)} className="w-full p-2 pl-10 text-sm text-gray-700" />
      </label>
      <button type="submit" className="bg-orange-500 hover:bg-orange-700 text-white font-bold py-2 px-4 rounded">
        Submit
      </button>
    </form>
  );
};

const Footer = () => {
  return (
    <footer className="bg-gray-200 h-screen pt-12 pb-6">
      <div className="container mx-auto p-4 pt-6 md:p-6 lg:p-12">
        <ul className="flex justify-center mb-4">
          <li>
            <a href="#" className="text-gray-600 hover:text-gray-900">
              Terms and Conditions
            </a>
          </li>
          <li>
            <a href="#" className="text-gray-600 hover:text-gray-900">
              Privacy Policy
            </a>
          </li>
          <li>
            <a href="#" className="text-gray-600 hover:text-gray-900">
              Contact Us
            </a>
          </li>
        </ul>
        <ul className="flex justify-center mb-4">
          <li>
            <a href="#" className="text-gray-600 hover:text-gray-900">
              <i className="fab fa-facebook-f" />
            </a>
          </li>
          <li>
            <a href="#" className="text-gray-600 hover:text-gray-900">
              <i className="fab fa-twitter" />
            </a>
          </li>
          <li>
            <a href="#" className="text-gray-600 hover:text-gray-900">
              <i className="fab fa-instagram" />
            </a>
          </li>
        </ul>
        <p className="text-gray-600 text-center">
          Copyright 2023 e-commerce website. All rights reserved.
        </p>
      </div>
    </footer>
  );
};

export default App;
'''
html_code = html_code_generator(react_code)
with open("index.html", "w", encoding="utf-8") as f:
    f.write(html_code.html_code) 

webbrowser.open("index.html")

