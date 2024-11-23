interface Iterator {
    public boolean hasnext();
    public Object next();
}

interface Container {
    public Iterator getIterator();
}

class NameRepository implements Container {
    public String names[] = {"Robert", "John", "Julie", "Lora"};

    @Override
    public Iterator getIterator() {
        return new NameIterator();
    }

    private class NameIterator implements Iterator {
        int index;

        @Override
        public boolean hasnext() {
            if (index < names.length) {
                return true;
            }

            return false;
        }

        @Override
        public Object next() {
            if (this.hasnext()){
                return names[index++];
            }
            return null;
        }
    }
}

public class IteratorTryout {
    
}