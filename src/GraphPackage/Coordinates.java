package GraphPackage;

public class Coordinates {

	Double x;
	
	Double y;

	

	public Coordinates(Double x, Double y) {
		super();
		this.x = x;
		this.y = y;
	}

	public Coordinates(Double number) {
		super();
		this.x = number;
	}

	public Double getX() {
		return x;
	}

	public void setX(Double x) {
		this.x = x;
	}

	public Double getY() {
		return y;
	}

	public void setY(Double y) {
		this.y = y;
	}

	@Override
	public String toString() {
		return "Coordinates [x=" + x + ", y=" + y + "]";
	}
	
	
}
