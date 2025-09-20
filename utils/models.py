from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Product:
    title: str
    subtitle: str
    part_number: str
    code: str
    stock: int
    price_usd: float
    price_pen: float
    image_url: str
    description: str
    url: str
    def __str__(self):
        content = [
            "***********************************************************************************",
            f"Producto: {self.title}",
            f"Subtitulo: {self.subtitle}",
            f"Número de Parte: {self.part_number}",
            f"Código Interno: {self.code}",
            f"Stock: {self.stock} UNDS.",
            f"Precio USD: {self.price_usd}",
            f"Precio S/.: {self.price_pen}",
            f"Enlace Imagen: {self.image_url}",
            f"Descripción: {self.description}",
            f"Enlace: {self.url}",
            "***********************************************************************************"
            ]
        return "\n".join(content)
                

@dataclass
class Section:
    title: str
    url: str
    children_number: int
    childs: List[str]
    image: Optional[str] = None
    def __str__(self):
        content = [
            "===================================================================================",
            f"Sección: {self.title}",
            f"URL: {self.url}",
            f"Cantidad de Categorías: {self.children_number}",
            f"Categorías: {self.childs}"
            "==================================================================================="
        ]
        return "\n".join(content)

@dataclass
class Category:
    title: str
    url: str
    image: Optional[str]
    products: List[Product]
    def __str__(self):
        content = [
          "###################################################################################",
          f"Categoría: {self.title}",
          f"Enlace: {self.url}",
          f"Enlace Imagen: {self.image}",
          "###################################################################################"  
        ]
        return "\n".join(content)