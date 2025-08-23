from datetime import datetime
from typing import List, Optional

class Tutorial:
    """Tutorial model for educational content"""
    
    def __init__(self, 
                 id: str,
                 title: str,
                 description: str,
                 category: str,
                 difficulty: str,
                 content: str,
                 tags: List[str],
                 created_at: Optional[datetime] = None,
                 updated_at: Optional[datetime] = None,
                 author: str = "Alireza Barzin Zanganeh",
                 estimated_read_time: int = 5,
                 prerequisites: List[str] = None,
                 image_url: str = None):
        """
        Initialize a Tutorial object
        
        Args:
            id: Unique identifier for the tutorial
            title: Tutorial title
            description: Short description of the tutorial
            category: Category (e.g., Machine Learning, Deep Learning, Statistics)
            difficulty: Difficulty level (Beginner, Intermediate, Advanced)
            content: Full tutorial content (markdown or HTML)
            tags: List of tags for categorization
            created_at: Creation timestamp
            updated_at: Last update timestamp
            author: Tutorial author name
            estimated_read_time: Estimated reading time in minutes
            prerequisites: List of prerequisite topics
            image_url: URL to tutorial cover image
        """
        self.id = id
        self.title = title
        self.description = description
        self.category = category
        self.difficulty = difficulty
        self.content = content
        self.tags = tags or []
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()
        self.author = author
        self.estimated_read_time = estimated_read_time
        self.prerequisites = prerequisites or []
        self.image_url = image_url or f"/static/images/tutorials/{id}.jpg"
    
    def to_dict(self) -> dict:
        """Convert tutorial to dictionary for JSON serialization"""
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'category': self.category,
            'difficulty': self.difficulty,
            'content': self.content,
            'tags': self.tags,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'author': self.author,
            'estimated_read_time': self.estimated_read_time,
            'prerequisites': self.prerequisites,
            'image_url': self.image_url,
            'url': f"/tutorial/{self.id}"
        }
    
    def get_difficulty_level(self) -> int:
        """Get numeric difficulty level for sorting"""
        difficulty_map = {
            'Beginner': 1,
            'Intermediate': 2,
            'Advanced': 3
        }
        return difficulty_map.get(self.difficulty, 1)
    
    def get_related_tutorials(self, all_tutorials: List['Tutorial'], limit: int = 3) -> List['Tutorial']:
        """Get related tutorials based on tags and category"""
        related = []
        
        # Find tutorials with matching tags
        for tutorial in all_tutorials:
            if tutorial.id == self.id:
                continue
                
            score = 0
            # Same category gets higher score
            if tutorial.category == self.category:
                score += 3
            
            # Shared tags get points
            shared_tags = set(self.tags) & set(tutorial.tags)
            score += len(shared_tags) * 2
            
            # Similar difficulty level
            if tutorial.difficulty == self.difficulty:
                score += 1
                
            if score > 0:
                related.append((tutorial, score))
        
        # Sort by score and return top matches
        related.sort(key=lambda x: x[1], reverse=True)
        return [tutorial for tutorial, score in related[:limit]]
    
    def update_content(self, new_content: str):
        """Update tutorial content and timestamp"""
        self.content = new_content
        self.updated_at = datetime.now()
    
    def add_tag(self, tag: str):
        """Add a tag if not already present"""
        if tag not in self.tags:
            self.tags.append(tag)
            self.updated_at = datetime.now()
    
    def remove_tag(self, tag: str):
        """Remove a tag if present"""
        if tag in self.tags:
            self.tags.remove(tag)
            self.updated_at = datetime.now()
    
    def __str__(self) -> str:
        return f"Tutorial: {self.title} ({self.category})"
    
    def __repr__(self) -> str:
        return f"Tutorial(id='{self.id}', title='{self.title}', category='{self.category}')"

# Example tutorial data factory
class TutorialFactory:
    """Factory class for creating tutorial instances"""
    
    @staticmethod
    def create_ml_tutorial(id: str, title: str, description: str, algorithm_type: str) -> Tutorial:
        """Create a machine learning tutorial with appropriate tags"""
        base_tags = ["machine-learning", "python", "scikit-learn"]
        
        if algorithm_type == "supervised":
            base_tags.extend(["supervised-learning", "prediction"])
        elif algorithm_type == "unsupervised":
            base_tags.extend(["unsupervised-learning", "clustering"])
        elif algorithm_type == "reinforcement":
            base_tags.extend(["reinforcement-learning", "agents"])
            
        return Tutorial(
            id=id,
            title=title,
            description=description,
            category="Machine Learning",
            difficulty="Intermediate",
            content="",
            tags=base_tags
        )
    
    @staticmethod
    def create_deep_learning_tutorial(id: str, title: str, description: str, network_type: str) -> Tutorial:
        """Create a deep learning tutorial with appropriate tags"""
        base_tags = ["deep-learning", "neural-networks", "python", "tensorflow", "pytorch"]
        
        if network_type == "cnn":
            base_tags.extend(["convolutional", "computer-vision", "image-processing"])
        elif network_type == "rnn":
            base_tags.extend(["recurrent", "sequence", "nlp", "time-series"])
        elif network_type == "transformer":
            base_tags.extend(["attention", "transformer", "bert", "gpt"])
            
        return Tutorial(
            id=id,
            title=title,
            description=description,
            category="Deep Learning",
            difficulty="Advanced",
            content="",
            tags=base_tags
        )
    
    @staticmethod
    def create_statistics_tutorial(id: str, title: str, description: str, stats_type: str) -> Tutorial:
        """Create a statistics tutorial with appropriate tags"""
        base_tags = ["statistics", "mathematics", "data-analysis", "python", "r"]
        
        if stats_type == "descriptive":
            base_tags.extend(["descriptive-stats", "visualization", "summary"])
        elif stats_type == "inferential":
            base_tags.extend(["hypothesis-testing", "confidence-intervals", "p-values"])
        elif stats_type == "bayesian":
            base_tags.extend(["bayesian", "prior", "posterior", "mcmc"])
            
        return Tutorial(
            id=id,
            title=title,
            description=description,
            category="Statistics",
            difficulty="Intermediate",
            content="",
            tags=base_tags
        )