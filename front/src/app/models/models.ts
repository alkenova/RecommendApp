export interface ICategory{
    id:number,
    name:string,
    created_at:any,
    description:string
}
export interface IProduct{
    id:number,
    name:string,
    image:string,
    description:string
}
export interface IAuthResponse{
    token: string;
}

export interface User {
    username: string;
    password: string;
}

export interface IUser {
    id: number;
    password: string;
    username: string;
    first_name: string;
    last_name: string;
    email: string;
    isMember: boolean; 
}