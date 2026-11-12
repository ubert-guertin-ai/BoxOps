function Component({ name }: {name: string}) {
  return (
    <h1>{name}</h1>
  )
}

export default function User() {
  return (
    <Component name="d" />
  )
}



