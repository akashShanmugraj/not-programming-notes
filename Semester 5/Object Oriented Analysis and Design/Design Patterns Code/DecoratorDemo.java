interface Cocoa {
    int sweet();
    int price();
    String desc();
}

class DarkChocolate implements Cocoa {
    @Override
    public int sweet() {
        return 50; 
    }

    @Override
    public int price() {
        return 10;
    }

    @Override
    public String desc() {
        return "Cocoa + Butter";
    }
}

abstract class CocoaDecorator implements Cocoa {
    protected Cocoa cocoaobject;

    public CocoaDecorator(Cocoa cocoa) {
        this.cocoaobject = cocoa;
    }

    @Override
    public int sweet() {
        return cocoaobject.sweet();
    }

    @Override
    public int price() {
        return cocoaobject.price();
    }

    @Override
    public String desc() {
        return cocoaobject.desc();
    }
}

class DarkChocolateDecorator extends CocoaDecorator {
    public DarkChocolateDecorator(Cocoa cocoa) {
        super(cocoa);
    }

    @Override
    public int sweet() {
        return cocoaobject.sweet() + 20;
    }

    @Override
    public int price() {
        return cocoaobject.price() + 10;
    }

    @Override
    public String desc() {
        return cocoaobject.desc() + ", butter";
    }
}

class MilkChocolateDecorator extends CocoaDecorator {
    public MilkChocolateDecorator(Cocoa cocoa) {
        super(cocoa);
    }

    @Override
    public int price() {
        return cocoaobject.price() + 15;
    }

    @Override
    public int sweet() {
        return cocoaobject.sweet() + 20;
    }

    @Override
    public String desc() {
        return cocoaobject.desc() + ", Butter, Sugar";
    }
}

class HotChocolateDecorator extends CocoaDecorator {
    public HotChocolateDecorator(Cocoa cocoa) {
        super(cocoa);
    }

    @Override
    public int price(){
        return cocoaobject.price() + 40;
    }

    @Override
    public int sweet() {
        return cocoaobject.sweet() + 25;
    }

    @Override
    public String desc() {
        return cocoaobject.desc() + ", Milk, Sugar";
    }
}

public class DecoratorDemo {
    
}
