export interface Waypoint {
    location: string;
    waypoint_type: 'Pickup' | 'Delivery';
}

export interface TransportOrder {
    order_number: string;
    customer_name: string;
    date: string;
    waypoints: Waypoint[];
    uuid?: string;
}

export interface PaginatedResponse<T> {
    count: number;
    next: string | null;
    previous: string | null;
    results: T[];
  }