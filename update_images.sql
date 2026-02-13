-- SQL script to update product images
UPDATE shop_product SET image = 'products/gardening-toolkit.jpg' 
WHERE name = 'AURA Premium Gardening Toolkit (8-in-1)';

UPDATE shop_product SET image = 'products/balcony-farming-kit.jpg' 
WHERE name = 'Beginner Balcony Farming Kit';

UPDATE shop_product SET image = 'products/microgreens-kit.jpg' 
WHERE name = 'Microgreens DIY Kit – 5 Varieties';

UPDATE shop_product SET image = 'products/potting-mix.jpg' 
WHERE name = 'Organic Vegetable Potting Mix 10kg';

UPDATE shop_product SET image = 'products/rakhi-eco-gift.jpg' 
WHERE name = 'Rakhi Eco-Gift Hamper with Plantable Seeds';

UPDATE shop_product SET image = 'products/corporate-desk-garden.jpg' 
WHERE name = 'Corporate Desk Garden Gift Box';

SELECT name, image FROM shop_product;
