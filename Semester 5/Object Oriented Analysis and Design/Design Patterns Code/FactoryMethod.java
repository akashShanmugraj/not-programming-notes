interface Person {
    void talk();
    void walk();
}

class NormalPerson implements Person {
    @Override
    public void talk() {
        System.out.println("talking");
    }

    @Override
    public void walk() {
        System.out.println("walking");
    }
}

class DumbPerson implements Person {
    @Override
    public void talk() {
        System.out.println("can't talk womp womp");
    }

    @Override
    public void walk() {
        System.out.println("walking");
    }
}

class DisabledPerson implements Person {
    @Override
    public void talk() {
        System.out.println("talking");
    }

    @Override
    public void walk() {
        System.out.println("can't walk womp womp");
    }
}

class PersonFactory {
    public Person getPerson(String persontype) {
        if (persontype == null) {
            return null;
        }

        if (persontype.equalsIgnoreCase("normal")){
            return new NormalPerson();
        } else if (persontype.equalsIgnoreCase("dumb")){
            return new DumbPerson();
        } else if (persontype.equalsIgnoreCase("disabled")){
            return new DisabledPerson();
        }

        return null;
    }
}

public class FactoryMethod {
    
}
